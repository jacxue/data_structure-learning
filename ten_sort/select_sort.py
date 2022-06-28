# -*- coding:utf-8 -*-
# 作者：薛晓通

"""
1.从左至右，检查数组的每个格子，用一个变量来记住检查过的最小值，如果后边的格子比当前记录还要小，那么索引指向最小的元素
2.与每个检查的开头进行交换，第一次检查是第0个，第二次是第一个
3.重复
"""


def select_sort(num):
    for i in range(len(num)):
        min_index = i
        for j in range(i+1, len(num)):
            if num[j] < num[min_index]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]


if __name__ == "__main__":
    num = [8, 5, 25, 96, 4, 15, 21]
    select_sort(num)
    print(num)