# -*- coding = utf-8 -*-
# @Time : 2021/4/28 22:52
# @Author : D-code
# @File : auto_enter.py
# @Software : PyCharm

def enter_title():
    a = []
    b = []
    with open('Title_part.txt', 'r', encoding='utf-8') as f:
        for line in f:
            a.append(line)
    for i in range(len(a)):
        a[i] = a[i].replace('\n', '')
        temp = a[i].split()
        for j in range(len(temp)):
            b.append(temp[j])
        b.append('.')
    # print(a)
    # print(b)
    with open('Title_enter.txt', 'w', encoding='utf-8') as f:
        for i in range(len(b)):
            if b[i] == '.':
                f.write('\n')
            else:
                f.write(b[i])
                f.write('\n')

def enter_abstract():
    content = []
    with open('Abstract_part.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        content = content.replace('.', ' .').replace(',', ' ,').replace('"', ' "').replace(':', ' :')
        abstract_list = content.split()
    # print(content)
    with open('Abstract_enter.txt', 'w', encoding='utf-8') as f:
        for i in range(len(abstract_list)):
            f.write(abstract_list[i])
            if abstract_list[i] == '.':
                f.write('\n')
            f.write('\n')


if __name__ == '__main__':
    enter_title()
    enter_abstract()
    print('换行成功！')
    input('按任意键退出...')