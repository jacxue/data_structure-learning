# -*- coding:utf-8 -*-
# 作者：薛晓通

def quick_sort(num, left, right):
    if left < right:
        mid = partition(num, left, right)
        quick_sort(num, 0, mid - 1)
        quick_sort(num, mid+1, right)
    return num


"""
# 把基准拿出来
左指针为第0个元素，右指针为最右边
# 在左右指针不相遇且右指针的比这个数大，则右指针想左移动；如果条件不满足，要把此时右指针位置的数字放到左边坑位
# 在左右指针不相遇且左指针的比这个数小，则左指针向右移动；如果条件不满足，要把此时左指针位置的数字放到右边坑位
# 最后把基准放到两指针相遇的位置
"""


def partition(num, left, right):
    temp = num[left]
    while left < right and num[right] >= temp:
        right -= 1
    num[left] = num[right]
    while left < right and num[left] <= temp:
        left += 1
    num[right] = num[left]
    num[left] = temp
    return left


if __name__ == "__main__":
    num = [90, 32, 34, 21, 14, 65, 87, 92, 18]
    quick_sort(num, 0, len(num) - 1)
    print(num)