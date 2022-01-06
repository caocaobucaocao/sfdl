from heap import heap_sort, left, right, an_build_max_heap
from test_util import build_random_list
from math import floor
from sys import maxsize

'''
T(n)=n*log(k)n,k=len(nums_list)
'''


def k_orderly_list_sort(nums_list):
    last_root = find_last_root(nums_list)
    for x in range(last_root, -1, -1):
        max_heapify(nums_list, x)
    count = 0
    for x in range(len(nums_list)):
        count = count + len(nums_list[x])
    res = list()
    for x in range(count):
        temp = extract_max(nums_list)
        if temp:
            res.append(temp)
        else:
            pass
    print(res)


def extract_max(nums_list):
    if not nums_list[0]:
        nums_list[0].append(-maxsize - 1)
        max_heapify(nums_list, 0)
        return
    else:
        max_heapify(nums_list, 0)
        return nums_list[0].pop(0)


def max_heapify(nums_list, index):
    value = nums_list[index][0]
    left_index = left(index, nums_list)
    if left_index is None:
        return
    else:
        left_value = nums_list[left_index][0]
        if value > left_value:
            return
        else:
            right_index = right(index, nums_list)
            if right_index is None:
                return
            else:
                right_value = nums_list[right_index][0]
                if left_value > right_value:
                    temp = nums_list[left_index]
                    nums_list[left_index] = nums_list[index]
                    nums_list[index] = temp
                    max_heapify(nums_list, left_index)
                else:
                    temp = nums_list[right_index]
                    nums_list[right_index] = nums_list[index]
                    nums_list[index] = temp
                    max_heapify(nums_list, right_index)


def find_last_root(nums_list):
    if len(nums_list) >= 2:
        return floor(len(nums_list) / 2) - 1
    elif len(nums_list) == 1:
        return
    else:
        return 0


def test_k_orderly_list_sort():
    nums_list = list()
    for t in range(3):
        temp = build_random_list()
        an_build_max_heap(temp)
        heap_sort(temp)
        temp.reverse()
        nums_list.append(temp)
    print(nums_list)
    print(k_orderly_list_sort(nums_list))


test_k_orderly_list_sort()
