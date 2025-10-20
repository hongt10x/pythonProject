# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250710-算法.py
@Time    : 2025/7/10 16:30
@Author  : Echo Wang
'''


def quick_sort(arr):
    '''快速排序算法，时间复杂度：平均 O(nlogn)，最坏 O(n**2)。'''
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(left, middle, right)
    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort(arr):
    '''冒泡排序算法，时间复杂度：最坏情况 O(n**2)，最优情况 O(n)（已排序时）。'''
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            print(arr[i], arr[j], arr[j + 1], arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
    return arr



def selection_sort(arr):
    '''选择排序算法，时间复杂度：始终为 O(n**2)。'''
    n = len(arr)
    for i in range(n):
        index_min = i
        for j in range(i + 1, n):
            print(j,arr[i], arr[index_min], arr)
            if arr[j] < arr[index_min]:
                index_min = j

        arr[i], arr[index_min] = arr[index_min], arr[i]
    return arr


if __name__ == '__main__':
    arr = [93, 12, 26, 69, 5, 88, 13, 55, 6, 7]
    # arr = [1, 3, 5, 6, 7, 9, 10]
    flag = 11
    if flag == 1:
        ...
        print(len(arr) // 2)
        print(quick_sort(arr))
    flag = 11
    if flag == 1:
        ...
        print(bubble_sort(arr))
    flag = 1
    if flag == 1:
        ...
        print(selection_sort(arr))
