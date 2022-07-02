# -*- coding:utf-8 -*-
# 作者：薛晓通

"""
1.创建一个双端队列
2.从中心点出发，把它的邻居加入队列
只要队列不为空
3.让队列最左端的出队，判断它是否满足它的条件，如果满足，退出循环
4.如果不满足，把它的邻居加入队列
直到找到目标或者队列为空为止
"""

from collections import deque

graph = {}


def person_is_seller(person):
    return person[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # 用于记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is finded")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

