---
bibliography: [1.bib]
csl: china-national-standard-gb-t-7714-2015-numeric.csl
nocite: /
    @*
---

\newcommand\degree{°}

# 摘    要{-}

中文摘要

\KeyWord{关键词1，关键词2，关键词3}

# **Abstract**{-}

English Abstract.

按照排版规定英文标题需要加粗

\KeyWord2{Key word 1, key word 2, key word 3}

\toc{目    录}

\newSection{UpperRoman}

# H1 Numbered

正文内容123

来点代码`some code`

来点代码`中文代码`

```python
if a == 1:
    print("str")
```

```text
纯文本测试
plain text
```

分割两段代码

```xml
<w:lvl w:ilvl="3">
    <w:start w:val="1"/>
    <w:numFmt w:val="decimalEnclosedCircleChinese"/>
    <w:pStyle w:val="4"/>
    <w:lvlText w:val="%4"/>
    <w:lvlJc w:val="left"/>
    <w:pPr>
        <w:ind w:left="0" w:firstLine="0"/>
    </w:pPr>
</w:lvl>
```

分割两段代码

```python
# 绝对素数.py
# 将自然数区间10-1000中所有绝对素数挑选出来，每行打印输出5个。绝对素数是：一个数和其反序数都是素数。
List = []  # 创建空数组
flag = 1
count = 0  # 计数器初始状态为0
for i in range(10, 1001):  # 自然数i在10-1000之间
    for j in range(2, i):
        if i % j == 0:  # 自然数i是否是素数
            flag = 0
            break  # 只要遇到一个因数，就可以不用进行后面的循环了
    if flag == 1:  # 如果经过上述判断flag还是1，说明正向是素数，现在判断反向素数
        s = str(i)
        m = int(s[::-1])
        for n in range(2, m):
            if m % n == 0:  # 自然数i的反序数m是否是素数
                flag = 0
                break  # 只要遇到一个因数，就可以不用进行后面的循环了
    if flag == 1:  # 将绝对素数全部添加至列表
        List.append(i)
    flag = 1
for k in List:  # 将list打印输出，五个一换行
    print(k, end=' ')
    count = count+1
    if count % 5 == 0:
        print('\n')

```

## H2 Numbered

正文内容123

![\Caption{fig}这里需要一个图片](nju.png)

### H3 Numbered

![\Caption{fig}题注需要中英双题注\newLine{} \Caption2{fig} Caption need both Chinese and English](nju.png)

#### H4 Numbered

参考文献也是需要的[@JifaLingling-132]

##### H5 Numbered

一条参考文献不够，再来两个一起试试[@Perner-171; @WeichselbraunGindl-160; @YangGuo-164]，\newLine{}怎么样，牛逼吧？

###### H6 Numbered

试试看公式呢。

勾股定理：设$\triangle ABC$顶点$A$，$B$，$C$的对边分别为 $a$，$b$，$c$，若成立 $$a^2+b^2=c^2$$ 则 $\triangle ABC$是直角三角形，且
$$ \angle ACB=90 \degree$$

$$a + b^2 = \frac{c}{d}$$ {#eq1}
$$\begin{matrix}α & β \\ 3 & 4 \\\end{matrix}$$
$$\begin{pmatrix}α & β \\ 3 & 4 \\\end{pmatrix}$$
$$\begin{bmatrix}α & β \\ 3 & 4 \\\end{bmatrix}$$

# H1 Unnumbered{-}

脚注也是规定论文的元素之一[^1]，再来   
一个脚注[^2]

> 测试一下引用\ref{eq1}

[^1]: 这是脚注1
[^2]: 这是脚注2

# 参考文献{-}

<!-- \Reference{} -->
::: {#refs}
:::

# 附录{- .appendix}

## A{- .appendix}

附录A中的内容

## B{- .appendix}

附录B中的内容
