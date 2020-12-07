## 运行

```text
pandoc example.md  --filter equations_no.py --filter section_break.py --filter header_convert.py -o example.docx
```

## 样式

除了 pandoc 预设的那几个样式外，还有以下几种特殊样式

- `TOC Heading`: 目录标题
- `Unnumbered Heading 1`: 无编号的一级标题
- `Unnumbered Heading 2`: 无编号的二级标题
- `Appendix Text`: 附录正文样式
- `Plain Text`: 无缩进的普通文本，用做公式编号的样式等
