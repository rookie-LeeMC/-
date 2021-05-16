# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

解题方法：
利用快排，不
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/3chong-jie-fa-miao-sha-topkkuai-pai-dui-er-cha-sou/#%E4%B8%89%E3%80%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B9%9F%E5%8F%AF%E4%BB%A5-%E8%A7%A3%E5%86%B3-topk-%E9%97%AE%E9%A2%98%E5%93%A6

堆
堆的本质是一个完全二叉树，新加入的元素先加到末尾，然后按规则上浮；
弹出元素后，堆顶元素赋值为末尾元素，然后按规则下沉；
最核心的是上浮和下沉两个方法



Heap是一种数据结构具有以下的特点：
1）完全二叉树；
2）heap中存储的值是偏序；

Min-heap: 父节点的值小于或等于子节点的值；
Max-heap: 父节点的值大于或等于子节点的值；

'''


def getLeastNumbers(arr, k):
    arr = sorted(arr, key=lambda x: x)
    return arr[:k]

# python的堆为最小堆
import heapq
def getLeastNumbers_v2(arr, k):
    # 特殊
    if not arr: return []

    heap=[]




arr = [3, 2, 1]
k = 2
getLeastNumbers(arr, k)
