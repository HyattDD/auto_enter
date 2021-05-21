# auto_enter使用说明
## 1.工具简介

- 本工具用于在处理原始材料科学文本语料过程中，将标题语料`Title_part`以及摘要语料`Abstract_part`进行处理，得到可以直接在`auto_ner`中执行的输入文件
- 环境：Windows(执行`.exe`文件) / Linux & Mac Os(执行`.py`文件)

## 2.文件说明

- `Abstract_part.txt`: 待处理的原始摘要文本
- `Title_part.txt`: 待处理的原始标题文本
- `Abstract_enter.txt`: 处理过后的摘要文本
- `Title_enter.txt`: 处理过后的标题文本
- `auto_enter`: 编译后的可执行文件
- `auto_enter.py`: python原始代码文件

## 3.处理规则

- 原始标题文本经过转换后，一行一个单词，每个标题结束后空一行，标题无句号
- 原始摘要文本经过转换后，一行一个单词，逗号、句号都占一行，每一句话结束后空一行

## 4.使用方法

- 将原始标题、摘要文本分别复制到`Title_part.txt`以及`Abstract_part.txt`中去
- 双击执行auto_enter.exe文件后，根据提示进行操作
- 处理后的文件自动生成在`Title_enter.txt`和`Abstract_enter.txt`文件中

## 5.问题反馈

- 使用中出现的问题可以联系donghaotian@tju.edu.cn

