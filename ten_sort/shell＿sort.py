# -*- coding:utf-8 -*-
# 作者：薛晓通

def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    # 初始步长
    gap = n // 2
    # gap变化到0之前，插入排序执行的次数
    while gap > 0:
        # 按步长进行插入排序、与普通的插入排序的区别就是步长
        for j in range(gap, n):
            i = j
            # 插入排序
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短步长
        gap = gap // 2


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    shell_sort(alist)
    print(alist)