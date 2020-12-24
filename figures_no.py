import panflute as pf
import copy
import re
top_level = 1

section_no = pf.RawInline(
    f'''<w:fldSimple w:instr=" STYLEREF {top_level} \s"/>''', format="openxml")
figure_no = pf.RawInline(
    f'''<w:fldSimple w:instr=" SEQ Figure \* ARABIC \s {top_level}"/>''',
    format="openxml")
figure_no2 = pf.RawInline(
    f'''<w:fldSimple w:instr=" SEQ Figure \c \* ARABIC \s {top_level} "/>''',
    format="openxml")
    # 重复上一个编号


class FigCaptionReplace():
    math_no = 1
    anchor_re = re.compile(r'{#([^}]+)}')

    def action(self, elem, doc):
        if isinstance(elem, pf.Image):
            # pf.debug("Image!")
            elem: pf.Image
            cap2_begin = False
            cap2 = []

            if '-' in elem.classes or 'unnumbered' in elem.classes:
                new_content = []
            else:
                new_content = [
                    pf.Str('图'), pf.Space,
                    pf.Span(section_no,
                            pf.Str('.'),
                            figure_no,
                            identifier=elem.identifier +
                            '-no' if elem.identifier else ""), pf.Space
                ]
            new_content.append(
                pf.Span(identifier=elem.identifier +
                        '-zh' if elem.identifier else ""))

            for elem1 in elem.content:
                if isinstance(
                        elem1, pf.RawInline
                ) and elem1.format == 'tex' and elem1.text == r'\Caption2{fig}':
                    new_content.append(pf.LineBreak)
                    if not ('-' in elem.classes
                            or 'unnumbered' in elem.classes):
                        new_content.extend(
                            (pf.Str('Fig.'), pf.Space, section_no, pf.Str('.'),
                             figure_no2, pf.Space))
                    new_content.append(
                        pf.Span(identifier=elem.identifier +
                                '-en' if elem.identifier else ""))
                    cap2_begin = True
                else:
                    new_content[-1].content.append(elem1)
            elem.content = new_content
        return elem

    def __init__(self):
        pass


def main(doc=None):
    replacer = FigCaptionReplace()
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == "__main__":
    main()
