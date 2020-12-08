import panflute as pf


class refsReplacer():
    def find(self, elem, doc=None):
        if hasattr(elem, 'identifier') and elem.identifier:
            self.bookmarks.add(elem.identifier)
            # pf.debug('anchor:', elem.identifier)
        return elem

    def replace(self, elem, doc):
        if isinstance(elem, pf.Cite):
            elem: pf.Cite
            citation: pf.Citation = elem.citations[0]
            # pf.debug(citation.id)
            if citation.id in self.bookmarks:
                elem = pf.RawInline(
                    f'<w:fldSimple w:instr=" REF {citation.id} \\h "/>',
                    format="openxml")
        return elem

    def __init__(self):
        self.bookmarks = set()


def main(doc=None):

    refs_replacer = refsReplacer()
    return pf.run_filters([refs_replacer.find, refs_replacer.replace], doc=doc)


if __name__ == "__main__":
    main()
