# -*- coding:utf-8 -*-
# 作者：薛晓通

"""
冒泡排序
1.两个指针指向两个相邻元素（开始即开头），比较大小
2.如果顺序错误（左边大于右边），互换位置
3.两指针右移一格
4.重复1-3操作，直至排好序为止
"""


def bubble_sort(num):
    unsorted_until_index = len(num) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if num[i] > num[i+1]:
                sorted = False
                num[i], num[i+1] = num[i+1], num[i]
        unsorted_until_index -= 1


def bubble_sort1(num):
    for i in range(len(num)-1):  # 控制伦茨
        for j in range(len(num)-i-1):  # 只需比较没有排好序的
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

if __name__ == "__main__":
    num = [8,32,15,21,6,54,2]
    bubble_sort1(num)
    print(num)