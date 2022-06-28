# -*- coding:utf-8 -*-
# 作者：薛晓通

"""
1.将索引1的位置暂时保存起来，用该索引缩编的值与其比较，如果大，则右移，暂时变量则放到空的位置
2.将索引2的位置保存起来，进行同样的操作
3.重复直至排序完毕
"""


def insert_sort(num):
    for index in range(1, len(num)):
        position = index
        tmp = num[index]
        while position > 0 and num[position - 1] > tmp:
            num[position] = num[position-1]
            position -= 1
        num[position] = tmp


if __name__ == "__main__":
    num = [4, 8, 90, 23, 56, 78, 42]
    insert_sort(num)
    print(num)