import panflute as pf
import copy

top_level = 2
equation_width = 0.7


def valign_block(width):
    return pf.RawBlock(
        f'<w:tcPr><w:vAlign w:val="center"/><w:tcW w:w="{width}" w:type="pct"/></w:tcPr>',
        format="openxml")


section_no = pf.RawInline(f'''<w:r>
    <w:fldChar w:fldCharType="begin"/>
    <w:instrText xml:space="preserve">StyleRef {top_level} \\s</w:instrText>
    <w:fldChar w:fldCharType="end"/><
    /w:r>''',
                          format="openxml")
equation_no = pf.RawInline(f'''<w:r>
    <w:fldChar w:fldCharType="begin"/>
    <w:instrText xml:space="preserve">Seq equations \\s {top_level}</w:instrText>
    <w:fldChar w:fldCharType="end"/>
    </w:r>''',
                           format="openxml")


class MathReplace():
    math_no = 1

    def action(self, elem, doc):
        pf.debug('s:', elem)
        if isinstance(elem, pf.Para):
            rows = []
            content_group = []
            for elem1 in elem.content:
                if isinstance(elem1, (pf.Space, pf.SoftBreak)):
                    if content_group and content_group[-1][0]:
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
                        math_caption = [
                            pf.Str('('), section_no,
                            pf.Str('.'), equation_no,
                            pf.Str(')')
                        ]
                        rows.append(
                            pf.TableRow(
                                pf.TableCell(
                                    valign_block(50 * (1 - equation_width))),
                                pf.TableCell(
                                    valign_block(100 * equation_width),
                                    pf.Para(math_elem)),
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
        pf.debug('o:', elem)
        return elem

    def __init__(self):
        pass


def main(doc=None):
    replacer = MathReplace()
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == "__main__":
    main()