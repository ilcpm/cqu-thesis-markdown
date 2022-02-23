---
type: "重庆大学本科毕业论文" # 页眉左上角的文字，可以直接改为研究生或者XXX作业（方便不写毕业论文的时候其他作业使用）可以改为空，但不能去掉！

singlePage: 1 # 是否单面打印，1单面，0双面，单双面的页眉不一样，通过这个参数确定

codeBlockNumbering: true # 对代码块添加行号
codeBlockNumberingMinLine: 3 # 只对超过该行数的代码块编号（最小0）
codeSpaceVisible: false # 在代码中使用字符U+2423（␣）显示空格（需要字体支持，否则可能导致字符宽度不一，效果极差，不建议使用）

autoEqnLabels: true # 自动编号公式
# tableEqns: false # 用表格编号公式，在预览时有效
autoTblLabels: true
autoFigLabels: true
autoThmLabels: true

# 题注相关的参数
# 将按照xxTitle chapter chapDelim item titleDelim的格式显示
# 例如：“图 1.2.3:这是图片题注”，“1.2”为标题编号即chapter，“3”对应item，
# 前缀“图 ”由figureTitle决定，标题编号“1.2”的深度由chapteresDepth决定
# “1.2”与“3”中间的点由chapDelim决定
# 题注前缀与题注文本的分隔符“:”由titleDelim决定
# 空格需要转义写成'&#32;'
chapters: true # 是否显示章节号
chaptersDepth: 1 # 标题编号深度，默认只有一级标题的编号
chapDelim: '.' # 编号chapter.item中间的“点”
figureTitle: "图&#32;"
figureTitle2: "Figure&#32;"
tableTitle: "表&#32;"
tableTitle2: "Table&#32;"
titleDelim: '&#32;' # 题注编号和题注文本之间的分隔符

# 公式编号格式为 eqPrefix chapter chapDelim item eqSuffix
# 例如："(4.1)"
eqPrefix: '('
eqSuffix: ')'

secondCaptionSeparator: "\\sc{}" # 题注中，双语题注的分隔符，需要使用"\sc{}"这样的LaTeX命令写法，需要转义
isParaAfterTable: true # 是否在表格之后自动生成空段落（CQU格式要求）

# 引用编号时的参数
figPrefix: 图
eqnPrefix: "("
tblPrefix: 表
secPrefix: "§"
pagePrefix: "第"
lstPrefix: "第"

figSuffix: ""
eqnSuffix: ")"
tblSuffix: ""
secSuffix: ""
pageSuffix: "页"
lstSuffix: "项"

# 定理环境相关
combineDefinitionTerm: true # 用Word中Crtl Alt Enter产生的能够合并两个段落的特殊段落标记合并定理的编号和内容
proof: "证明　"
proofQed: '[□]{style="Definition Qed"}' # 这里对“方框”套用了文本样式“Definition Qed”

theoremSeparator: "　" # 定理环境的前缀与定理之间的分隔符，默认为全角空格
# 定理环境的标题（如果有）的前后缀
# （例如：“定理 1.2 (勾股定理)”中的“勾股定理”）
theoremPrefix: "&#32;("
theoremSuffix: ")"
# 定理环境各项内容的前缀字符定义
theorems:
  assumption: "假设&#32;"
  definition: "定义&#32;"
  defn: "定义&#32;"
  proposition: "命题&#32;"
  prop: "命题&#32;"
  lemma: "引理&#32;"
  lem: "引理&#32;"
  theorem: "定理&#32;"
  thm: "定理&#32;"
  axiom: "公理&#32;"
  corollary: "推论&#32;"
  cor: "推论&#32;"
  exercise: "练习&#32;"
  example: "例&#32;"
  exmp: "例&#32;"
  remark: "注释&#32;"
  rem: "注释&#32;"
  problem: "问题&#32;"
  conjecture: "猜想&#32;"

# 指定 docx 文件所在的绝对路径（在 Unix-like 系统或 WSL 上使用时，用于指定对应 Windows 路径）
workPath: ""

---
\newcommand\pageInfo{<w:pgSz w:w="11907" w:h="16840" w:code="9"/><w:pgMar w:top="1701" w:right="1418" w:bottom="1418" w:left="1418" w:header="907" w:footer="851" w:gutter="567"/><w:footnotePr><w:numFmt w:val="decimalEnclosedCircleChinese"/><w:numRestart w:val="eachPage"/></w:footnotePr>}

\newcommand\newSection{\newSectionRaw{\pageInfo}}

\newcommand\newSectionAbstract{\newSectionRaw{<w:pgNumType w:fmt="upperRoman" w:start="1"/><w:headerReference w:type="even" r:id="rId9"/><w:headerReference w:type="default" r:id="rId12"/><w:footerReference w:type="even" r:id="rId16"/><w:footerReference w:type="default" r:id="rId15"/><w:headerReference w:type="first" r:id="rId10"/><w:footerReference w:type="first" r:id="rId14"/>\pageInfo}}

\newcommand\newSectionTOC{\newSectionRaw{<w:pgNumType w:fmt="upperRoman" /><w:headerReference w:type="even" r:id="rId13"/><w:headerReference w:type="default" r:id="rId11"/>\pageInfo}}

\newcommand\toc{\tocRaw{目    录}}
