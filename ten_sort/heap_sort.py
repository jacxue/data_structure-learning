# -*- coding:utf-8 -*-
# 作者：薛晓通

# 调整函数
def sift(li, low, high):
    """
    low:根节点位置
    high：最后一个叶节点位置
    """
    i = low  # 指向根节点位置
    tmp = li[low]  # 把堆顶元素拿出来
    j = 2 * i + 1  # 左子节点位置
    while j <= high:  # 子节点不越界时
        if j + 1 <= high and li[j+1] > li[j]:  # 如果右节点存在并且比左节点大
            j = j+1  # 把j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]  # 把j放到原来的位置
            i = j  # 更新i
            j = 2*i + 1  # 跟着更新j
        else:
            li[i] = tmp  # 如果拿出来的元素比子节点大，放回原位
            break
    else:
        li[i] = tmp  # 如果j越界，把tmp放到村民位置


def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):  # 每个小堆的堆顶，
        sift(li, i, n-1)  # 从下往上进行调整
        # 建堆完成
    for i in range(n-1, -1, -1):  # 新堆得最后一个元素位置
        li[0], li[i] = li[i], li[0]  # 与堆顶元素交换
        sift(li, 0, i-1)  # 调整，i-1是新的边界
    return li


if __name__ == "__main__":
    li = [10, 3, 2, 7, 4, 9, 3, 6, 8, 21]
    print(heap_sort(li))
