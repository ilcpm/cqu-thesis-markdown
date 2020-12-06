## 运行

```
pandoc example.md  --filter equations_no.py --filter section_break.py -o example.docx
```

## 样式

除了 pandoc 预设的那几个样式外，还有以下几种特殊样式

- `Unnumbered Header 1`: 无编号的一级标题
- `Appendix Header N`(N = 2, 3, ...): 附录的第 N 级标题
- `TOC Heading`: 目录标题
- `Equation Caption`: 公式编号

