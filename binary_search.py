# -*- coding:utf-8 -*-
# 作者：薛晓通
import time


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        # 只要low和high没有缩小到只剩一个元素
        mid = (low + high) // 2
        guess = list[mid]
        print(guess)
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    a = time.time()
    list = [i for i in range(129)]
    print(binary_search(list, 128))
    b = time.time()
    print(b - a)