# 摘要 {-}

中文摘要

\KeyWord{关键词1，关键词2}

# Abstract {-}

英文摘要

\KeyWord2{Keyword1, keyword2}

\toc{目   录}

\newSection{UpperRoman}

# 有序号章节1

代码原文：

``` 
解以下方程组：$$x=y+1$$ $$2x=y$$ 
得 $$\begin{cases}x=-1\\y=-2\end{cases}$$
```

解以下方程组：$$x=y+1$$ $$2x=y$$ 
得 $$\begin{cases}x=-1\\y=-2\end{cases}$$ {#abc} 这个公式有标签`abc`

下面的公式无编号：
$$ x=y $${-}

以下两个公式后有`{#a}`:$$x=y_0$${} {#a} $$x=y_1$$ {} {#a}

# 有序号章节2

方程组$$ \begin{cases} x=y\\x=y+1\end{cases} $$ 无解！

图 1：单语有标签 `fig1`（编号标签`fig1-no`，中文标题标签`fig1-zh`）

![单语](cqu.png){#fig1 width=25%}

图 2：双语有标签 `fig2`（同图 1，外加英文标题标签`fig2-en`）

![中文\Caption2{fig}English](cqu.png){#fig2 width=25%}

图 3：无编号双语标签

![中文\Caption2{fig}English](cqu.png){- width=25%}

图 [@fig1-no]，其标题为[@fig1-zh]；图[@fig2-no]，其中文标题为[@fig2-zh]，英文标题为[@fig2-en]。

## 有序号章节3

下面有一个空段落`\newPara`:

\newPara

下面有三个空段落`\newPara{3}`:

\newPara{3}

这就是`\newPara`。

# 参考文献 {.refs}

::: {#refs}
:::

# 附录 {.appendix}

## 作者在攻读博士学位期间发表的论文目录

论文

## 作者在攻读博士学位期间参加的科研项目及得奖情况

获奖

# 致谢 {.thanks}
