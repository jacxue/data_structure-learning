# -*- coding:utf-8 -*-
# 作者：薛晓通

"""
牺牲空间换时间，从0到max统计每个数出现了几次，然后再输出就排序好了
适用于竖直再一定范围内的排序，比如按照人的年龄排序，0-150岁
"""


def counting_sort(array):
    if len(array) <= 1:
        return array
    # 找到最大值
    max_num = max(array)
    # 创建统计数组，索引是数字，值是统计的个数
    count = [0] * (max_num + 1)
    for num in array:
        count[num] += 1
    new_array = list()
    for i in range(len(count)):  # 控制要输出的值
        for j in range(count[i]):  # 控制添加次数
            new_array.append(i)
    return new_array


if __name__ == '__main__':
    array = [3, 5, 3, 1, 1, 2, 2, 5, 5, 5, 4, 4]
    print(counting_sort(array))
