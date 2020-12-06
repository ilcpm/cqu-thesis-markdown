import panflute as pf
import typing
index_str = "目录"

const_commands = {
    r'\newLine':
    pf.LineBreak(),
    r'\t':
    pf.Str('\t'),
    r'\newPage':
    pf.RawBlock("<w:p><w:r><w:br w:type=\"page\" /></w:r></w:p>",
                format="openxml"),
    r'\tabL':
    pf.RawInline(
        '<w:r><w:ptab w:relativeTo="margin" w:alignment="left" w:leader="none"/></w:r>',
        format="openxml"),
    r'\tabR':
    pf.RawInline(
        '<w:r><w:ptab w:relativeTo="margin" w:alignment="right" w:leader="none"/></w:r>',
        format="openxml"),
    r'\tabC':
    pf.RawInline(
        '<w:r><w:ptab w:relativeTo="margin" w:alignment="center" w:leader="none"/></w:r>',
        format="openxml"),
    r'\tab':
    pf.RawInline("<w:r><w:tab/></w:r>", format="openxml")
}


def toc(title=index_str):
    return [
        pf.Div(pf.Para(pf.Str(title)),
               attributes={"custom-style": "TOC Heading"}),
        pf.RawBlock(
            r"""<w:p><w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText>TOC \o "1-3" \h \z \u</w:instrText></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>"""
        )
    ]


def newSection(fmt: str = "", start: str = ""):
    fmtstr = f'w:fmt="{fmt}"' if fmt else ""
    startstr = f'w:start="{start}"' if start else ""
    pagestr = f'<w:pgNumType {fmtstr} {startstr}/>' if startstr or fmtstr else ""
    return pf.RawBlock(
        f"<w:p/><w:p><w:pPr><w:sectPr>{pagestr}</w:sectPr></w:pPr></w:p>",
        format="openxml")


class ConstTexCommandReplace():
    def action(self, elem, doc):
        pf.debug('s:', elem)
        if isinstance(elem, (pf.RawBlock, pf.RawInline)):
            text = elem.text if elem.text[-2:] != "{}" else elem.text[:-2]
            #pf.debug(text)
            if elem.format == 'tex':
                if text in self.commands:
                    method = self.commands[text]
                    elem = method
                else:
                    elem = eval(
                        elem.text.replace("{", "(", 1).replace(
                            '\\', '', 1)[::-1].replace("}", ")", 1)[::-1])

        pf.debug('o:', elem)
        return elem

    def __init__(self, comands):
        self.commands = comands


def main(doc=None):
    replacer = ConstTexCommandReplace(comands=const_commands)
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == "__main__":
    main()
