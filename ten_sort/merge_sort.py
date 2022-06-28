# -*- coding:utf-8 -*-
# 作者：薛晓通


"""
# 1.实现merge操作
# 使用两个指针，比较两个排序好的列表
# 在两个指针都不越界的情况下
# 如果左边小于等于右边，那么左边添加到列表
# 否则右边添加添加到列表
# 循环条件不满足的时候，把剩下的元素写到列表中

# 2.实现merge_sort操作
# 如果列表只有一个元素，直接返回这个列表
# 计算中间值，进行切片操作，分成两个小的列表
# 调用自己
# 调用merge
"""


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq)//2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == "__main__":
    seq = [7, 34, 63, 22, 12, 31, 34]
    seq = merge_sort(seq)
    print(seq)