import panflute as pf
top_level = 2
index_str = "目录"


def toc(title=index_str):
    return [
        pf.Div(pf.Para(pf.Str(title)),
               attributes={"custom-style": "TOC Heading"}),
        pf.RawBlock(r"""<w:sdt>
        <w:sdtPr>
        <w:docPartObj>
        <w:docPartGallery w:val="Table of Contents"/>
        <w:docPartUnique/>
        </w:docPartObj>
        </w:sdtPr>
        <w:sdtContent>
        <w:p><w:r>
        <w:fldChar w:fldCharType="begin" w:dirty="true"/>
        <w:instrText xml:space="preserve">TOC \o "1-3" \h \z \u</w:instrText>
        <w:fldChar w:fldCharType="separate"/>
        <w:fldChar w:fldCharType="end"/>
        </w:r></w:p></w:sdtContent>""",
                    format="openxml")
    ]


def newSection(fmt: str = "", start: str = ""):
    fmtstr = f'w:fmt="{fmt}"' if fmt else ""
    startstr = f'w:start="{start}"' if start else ""
    pagestr = f'<w:pgNumType {fmtstr} {startstr}/>' if startstr or fmtstr else ""
    return pf.RawBlock(
        f"<w:p><w:pPr><w:sectPr>{pagestr}</w:sectPr></w:pPr></w:p>",
        format="openxml")


class AutoSectionBreak():
    def __init__(self):
        self.section_begined = False
        self.refs_begined = False
        self.after_section_begined = False

    def action(self, elem, doc):
        if isinstance(elem, pf.Header) and elem.level == top_level:
            if 'chinese-abstract' in elem.classes:
                pass
            elif 'english-abstract' in elem.classes:
                elem = [newSection(fmt="upperRoman", start="1"), elem]
            elif 'refs' in elem.classes:
                self.refs_begined = True
                elem = [newSection(fmt="decimal"), elem]
            elif not self.section_begined:
                self.section_begined = True
                elem = [
                    newSection(fmt="upperRoman"),
                    pf.Div(*toc(), identifier='index'),
                    newSection(fmt="upperRoman"), elem
                ]
            else:
                if not self.after_section_begined:
                    elem = [newSection(fmt="decimal", start="1"), elem]
                    self.after_section_begined = True
                else:
                    elem = [newSection(fmt="decimal"), elem]
        return elem


def main(doc=None):
    replacer = AutoSectionBreak()
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == "__main__":
    main()
