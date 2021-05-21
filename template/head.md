---
bibliography: [1.bib]  # 参考文献信息文件（通过这个文件提供参考文献的引入支持）
csl: china-national-standard-gb-t-7714-2015-numeric.csl  # 参考文献的样式文件（通过这个文件确定参考文献的显示样式）
# 下面这个参数固定，表示把.bib文件中未使用的参考文献也一并插入文档
nocite: /
    @*
type: "重庆大学本科毕业论文" # 页眉左上角的文字，可以直接改为研究生或者XXX作业（方便不写毕业论文的时候其他作业使用）可以改为空，但不能去掉！

# 题注相关的参数
# 将按照title chapter chapDelim item titleDelim的格式显示
# 例如：“图 1.2.3:这是图片题注”，“1.2”为标题编号即chapter，“3”对应item，
# 前缀“图 ”由figureTitle决定，标题编号“1.2”的深度由chapteresDepth决定
# “1.2”与“3”中间的点由chapDelim决定
# 题注前缀与题注文本的分隔符“:”由titleDelim决定
# 空格需要转义为'&#32;'
chapters: true # 是否显示章节号（还没做）
chaptersDepth: 1 # 标题编号深度，默认只有一级标题的编号
chapDelim: '.' # 编号chapter.item中间的“点”
figureTitle: "图&#32;"
figureTitle2: "Figure&#32;"
tableTitle: "表&#32;"
tableTitle2: "Table&#32;"
titleDelim: '&#32;' # 题注编号和题注文本直接的分隔符

# 下方参数目前尚未实现
# 引用编号时的参数
figPrefix: 图
eqnPrefix: 式
tblPrefix: 表
secPrefix: 节
---
\newcommand\pageInfo{<w:pgSz w:w="11907" w:h="16840" w:code="9"/><w:pgMar w:top="1701" w:right="1418" w:bottom="1418" w:left="1418" w:header="907" w:footer="851" w:gutter="567"/><w:footnotePr><w:numFmt w:val="decimalEnclosedCircleChinese"/><w:numRestart w:val="eachPage"/></w:footnotePr>}

\newcommand\newSectionAbstract{\newSection{<w:pgNumType w:fmt="upperRoman" w:start="1"/><w:headerReference w:type="even" r:id="rId9"/><w:headerReference w:type="default" r:id="rId12"/><w:footerReference w:type="even" r:id="rId16"/><w:footerReference w:type="default" r:id="rId15"/><w:headerReference w:type="first" r:id="rId10"/><w:footerReference w:type="first" r:id="rId14"/>\pageInfo}}

\newcommand\newSectionTOC{\newSection{<w:pgNumType w:fmt="upperRoman" /><w:headerReference w:type="even" r:id="rId13"/><w:headerReference w:type="default" r:id="rId11"/>\pageInfo}}

\newcommand\toc{\tocRaw{目    录}}
