import panflute as pf
import copy
import re
top_level = 1
equation_width = 0.7


def valign_block(width):
    return pf.RawBlock(
        f'<w:tcPr><w:vAlign w:val="center"/><w:tcW w:w="{width}" w:type="pct"/></w:tcPr>',
        format="openxml")


section_no = pf.RawInline(f'''<w:fldSimple w:instr=" STYLEREF {top_level} \s"/>''',
                          format="openxml")
equation_no = pf.RawInline(f'''<w:fldSimple w:instr=" SEQ Equation \* ARABIC \s {top_level}"/>''',
                           format="openxml")
figure_no = pf.RawInline(f'''<w:fldSimple w:instr=" SEQ Figure \* ARABIC \s {top_level}"/>''',
                           format="openxml")


class MathReplace():
    math_no = 1
    anchor_re = re.compile(r'{#([^}]+)}')

    def action(self, elem, doc):
        # pf.debug('s:', elem)
        if isinstance(elem, pf.Para):
            rows = []
            content_group = []
            for elem1 in elem.content:
                if content_group and content_group[-1][0]:
                    if isinstance(elem1, (pf.Space, pf.SoftBreak)):
                        continue
                    elif isinstance(elem1, pf.Str) and isinstance(
                            content_group[-1][1][-1], pf.Math):
                        if elem1.text == '{}':
                            content_group[-1][1][-1] = (
                                content_group[-1][1][-1], None)
                            continue
                        elif elem1.text == '{.notag}' or elem1.text == '{-}':
                            content_group[-1][1][-1] = (
                                content_group[-1][1][-1], "")
                            continue
                        else:
                            match = self.anchor_re.match(elem1.text)
                            if match:
                                content_group[-1][1][-1] = (
                                    content_group[-1][1][-1], match[1])
                                continue
                is_math = isinstance(elem1,
                                     pf.Math) and elem1.format == 'DisplayMath'
                if content_group:
                    if content_group[-1][0] == is_math:
                        content_group[-1][1].append(elem1)
                        continue
                content_group.append([is_math, [elem1]])
            elem_old = elem
            elem = []
            for elem_group in content_group:
                if elem_group[0]:
                    rows = []
                    for math_elem in elem_group[1]:
                        if isinstance(math_elem, pf.Math):
                            math_elem = math_elem
                            notag = False
                            tag = ''
                        else:
                            if isinstance(math_elem[1], str):
                                if math_elem[1]:
                                    tag = math_elem[1]
                                    notag = False
                                else:
                                    tag = ''
                                    notag = True
                                    # pf.debug('notag')
                                math_elem = math_elem[0]
                            else:
                                math_elem = math_elem[0]
                                notag = False
                                tag = ''
                        math_caption = [
                            pf.Span(pf.Str('('),section_no,
                                    pf.Str('.'),
                                    equation_no,
                                    pf.Str(')'),
                                    identifier=tag
                            )
                        ] if not notag else []

                        rows.append(
                            pf.TableRow(
                                pf.TableCell(
                                    valign_block(50 * (1 - equation_width))),
                                pf.TableCell(
                                    valign_block(100 * equation_width),
                                    pf.Div(pf.Para(math_elem),
                                           attributes={
                                               'custom-style':
                                               'Equation'
                                           })),
                                pf.TableCell(
                                    valign_block(50 * (1 - equation_width)),
                                    pf.Div(pf.Para(*math_caption),
                                           attributes={
                                               'custom-style':
                                               'Equation Caption'
                                           }))))
                        self.math_no += 1
                    elem.append(
                        pf.Table(pf.TableBody(*rows),
                                 colspec=[
                                     ('AlignLeft', (1 - equation_width) / 2),
                                     ('AlignLeft', equation_width),
                                     ('AlignRight', (1 - equation_width) / 2)
                                 ],
                                 caption=pf.Caption(pf.Div())))
                else:
                    elem_new = copy.copy(elem_old)
                    elem_new.content = elem_group[1]
                    elem.append(elem_new)
        # pf.debug('o:', elem)
        return elem

    def __init__(self):
        pass


def main(doc=None):
    replacer = MathReplace()
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == "__main__":
    main()
