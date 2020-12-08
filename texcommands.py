import panflute as pf
import typing
import re
index_str = "目录"

pageInfoStr = r'''<w:pgSz w:w="11907" w:h="16840" w:code="9"/><w:pgMar w:top="1134" w:right="1418" w:bottom="1418" w:left="1418" w:header="907" w:footer="851" w:gutter="567"/>'''

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
    pf.RawInline("<w:r><w:tab/></w:r>", format="openxml"),
    r'\newSection{UpperRoman}':
    pf.RawBlock(
        r"""<w:p><w:pPr><w:sectPr><w:pgNumType w:fmt="upperRoman" w:start="1"/>"""
        + pageInfoStr + r"""</w:sectPr></w:pPr></w:p>""",
        format="openxml"),
    r'\newSection{Arabic}':
    pf.RawBlock(
        f"""<w:p><w:pPr><w:sectPr><w:pgNumType w:fmt="decimal" w:start="1"/>"""
        + pageInfoStr + r"""</w:sectPr></w:pPr></w:p>""",
        format="openxml"),
    r'\toc{目    录}': [
        pf.Div(pf.Para(pf.Str("目    录")),
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
        </w:r></w:p></w:sdtContent></w:std>""",
                    format="openxml")
    ],
    r'\ref{eq1}':
    pf.RawInline(r"""<w:fldSimple w:instr=" REF eq1 \h "/>""",
                 format="openxml"),
    r'\Caption2{fig}':
    pf.RawInline(
        r"""<w:r><w:t>Figure</w:t></w:r><w:fldSimple w:instr=" STYLEREF 1 \s"/><w:r><w:t>.</w:t></w:r><w:fldSimple w:instr=" SEQ Figure \c "/>""",
        format="openxml"),
    r'\Caption{fig}':
    pf.RawInline(
        r"""<w:r><w:t>图</w:t></w:r><w:fldSimple w:instr=" STYLEREF 1 \s"/><w:r><w:t>.</w:t></w:r><w:fldSimple w:instr=" SEQ Figure \* ARABIC \s 1 "/>""",
        format="openxml"),
}


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
        </w:r></w:p></w:sdtContent></w:std>""",
                    format="openxml")
    ]


fun_commands = {
    'refs':
    lambda x: pf.RawInline(f'<w:fldSimple w:instr=" REF {x} \\h "/>',
                           format="openxml"),
    'KeyWord':
    lambda x: pf.Para(
        pf.Span(pf.Str("关键词："), attributes={'custom-style': 'Key Word'}),
        pf.Str(x)),
    'KeyWord2':
    lambda x: pf.Para(
        pf.Span(pf.Str("Keywords: "), attributes={'custom-style': 'Key Word'}),
        pf.Str(x)),
    'toc':
    toc
}


def newSection(fmt: str = "", start: str = ""):
    fmtstr = f'w:fmt="{fmt}"' if fmt else ""
    startstr = f'w:start="{start}"' if start else ""
    pagestr = f'<w:pgNumType {fmtstr} {startstr}/>' if startstr or fmtstr else ""
    return pf.RawBlock(
        f"<w:p><w:pPr><w:sectPr>{pagestr}</w:sectPr></w:pPr></w:p>",
        format="openxml")


class ConstTexCommandReplace():
    tex_re = re.compile(r'\\([^{ ]*)(?:{(.*)})? ?')

    def action(self, elem, doc):
        # pf.debug('s:', elem)
        if isinstance(elem, (pf.RawBlock, pf.RawInline)):
            text = elem.text if elem.text[-2:] != "{}" else elem.text[:-2]
            text = text.strip()
            if elem.format == 'tex':
                if text in self.const_commands:
                    elem = self.const_commands[text]
                else:
                    pf.debug(elem)
                    re_result = self.tex_re.fullmatch(elem.text)
                    if re_result:
                        if re_result[1] in self.commands:
                            elem = self.commands[re_result[1]](re_result[2])

        # pf.debug('o:', elem)
        return elem

    def __init__(self, const_comands, commands):
        self.const_commands = const_comands
        self.commands = commands


def main(doc=None):
    replacer = ConstTexCommandReplace(const_comands=const_commands,
                                      commands=fun_commands)
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == "__main__":
    main()
