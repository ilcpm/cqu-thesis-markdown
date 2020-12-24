# find(): 对[xxx]{#abc}这样的写法标记书签
# replace(): 对[@xxx]这样的写法引用书签
# 可以实现对标题编号的引用
# 写代码记得写注释！！！
# TODO 引用嵌套怎么办？？？

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
            citationId: str = citation.id
            if citation.id in self.bookmarks:
                elem = pf.RawInline(
                    f'<w:fldSimple w:instr=" REF {citation.id} \\h "/>',
                    format="openxml")
            elif citationId.startswith('sec-'):
                # 对标题的编号引用处理 [@sec-xxx] [@sec-xxx-no]
                if citationId.endswith('-no'):
                    elem = pf.RawInline(f'<w:fldSimple w:instr=" REF {citationId[4:-3]} \\r \\h "/>',
                                        format="openxml")
                else:
                    elem = pf.RawInline(f'<w:fldSimple w:instr=" REF {citationId[4:]} \\h "/>',
                                        format="openxml")
            elif citationId.startswith('page-'):
                # 对页码的引用进行处理
                elem = pf.RawInline(f'<w:fldSimple w:instr=" PAGEREF {citationId[5:]} \\h "/>',
                                    format="openxml")
        return elem

    def __init__(self):
        self.bookmarks = set()


def main(doc=None):

    refs_replacer = refsReplacer()
    return pf.run_filters([refs_replacer.find, refs_replacer.replace], doc=doc)


if __name__ == "__main__":
    main()
