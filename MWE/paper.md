---
bibliography: [refs.bib]
# 参考文献信息文件（通过这个文件提供参考文献的引入支持），这是一个列表，可以通过`[a.bib, b.bib]`的格式使用多个bib参考文件
csl: china-national-standard-gb-t-7714-2015-numeric.csl  # 参考文献的样式文件（通过这个文件确定参考文献的显示样式），理科采用的是“编号”格式的参考文献格式
# 下面这个参数固定，表示把.bib文件中未使用的参考文献也一并插入文档
nocite: /
    @*

# 中英文关键词
keywords: ["排版", "论文", "格式转换"]
keywords-en: ["pandoc", "markdown", "word"]
---

# 摘\Space{2}要{-}

在此处撰写中文摘要

\newPara{}

\cKeyWords{}

# **ABSTRACT**{-}

在此处撰写英文摘要

\newPara{}

\eKeyWords{}

\newSectionAbstract

\toc

<!-- 如需要图目录和表目录，请删除该行
\Style{TOC}图目录

`{ TOC \h \z \c "图" \x}`{=field}

\Style{TOC}表目录

`{ TOC \h \z \c "表" \x}`{=field}
再删除这行 -->

\newSectionTOC

# 正文

这是一个最小工作示例（MWE），无任何多余内容，可直接在此文件上撰写论文。

This is a MWE. MWE stands for Minimum Working Example.

# 参考文献{-}

\Reference{}

# 附录{.appendix}

## 附录A

附录正文

# 致\Space{2}谢{-}
