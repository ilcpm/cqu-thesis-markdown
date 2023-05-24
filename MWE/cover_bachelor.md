---
author: '张三'
author-en: 'ilcpm'
student-id: '20170000'
teacher: '李四'
teacher-en: 'Hagb'
assistant-teacher: '王五'
assistant-teacher-en: 'Ruossipha'
major: '信息与计算科学'
major-en: 'Computer Science'
college: '重庆大学数学与统计学院'
college-en: 'Mathematics and Statistics Department\newLine{}Chongqing University'
date: 2023-06-01

title: '基于pandoc的Markdown到Word论文转换方案'
title-en: 'A Method of Converting Markdown to Word Using Pandoc'
---
:::{style="Title"}
重庆大学本科学生毕业论文（设计）
:::

\newPara{2}

:::{style="Subtitle"}
\metadata{title}
:::

\newPara{2}

![](CQU_logo.png){width=3.35cm height=3.35cm}

\newPara{3}

:::{style="Author"}
| \tab{}学　　生：\tab{}\metadata{author}
| \tab{}学　　号：\tab{}\metadata{student-id}
| \tab{}指导教师：\tab{}\metadata{teacher}
| \tab{}助理指导教师：\metadata{assistant-teacher}
| \tab{}专　　业：\tab{}\metadata{major}
:::

\newPara{2}

:::{style="Title"}
\metadata{college}
:::

:::{style="Date"}
\cdate{}
:::

\newSection{}

:::{style="Title"}
**Graduation Thesis (Design) of Chongqing University**
:::

\newPara{2}

:::{style="Subtitle"}
**\metadata{title-en}**
:::

\newPara{2}

![](CQU_logo.png){width=3.35cm height=3.35cm}

\newPara{3}

:::{style="Author"}
| \tab{}**Undergraduate: \metadata{author-en}**
| \tab{}**Supervisor: \metadata{teacher-en}**
| \tab{}**Assistant Supervisor: \metadata{assistant-teacher-en}**
| \tab{}**Major: \metadata{major-en}**
| \tab{}
:::

\newPara{1}

:::{style="Title"}
**\metadata{college-en}**
:::

:::{style="Date"}
**\edate{}**
:::

\newSection{}
