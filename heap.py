from math import floor, ceil
from sys import maxsize

'''
    T(n)=n*logn
'''


def heap_sort(num_list):
    bar = len(num_list) - 1
    for x in range(len(num_list) - 1, -1, -1):
        if x < 1:
            break
        temp = num_list[x]
        num_list[x] = num_list[0]
        num_list[0] = temp
        bar -= 1
        max_heapify(num_list, 0, bar)


'''
    T(n）=n
'''


def build_max_heap(num_list):
    index = find_last_root(num_list)
    bar = len(num_list) - 1
    for x in range(index, -1, -1):
        max_heapify(num_list, x, bar)


'''
    T(n)=n
'''


def an_build_max_heap(num_list):
    for key in range(len(num_list)):
        heapify_increase_key(num_list, key, num_list[key])


'''
    T(N）=logn
'''


def max_heapify(num_list, index, bar):
    value = num_list[index]
    left_index = left(index, num_list)
    if not left_index or left_index > bar:
        return
    left_value = num_list[left_index]
    right_index = right(index, num_list)
    if right_index:
        if right_index > bar:
            if left_index > bar:
                return
            else:
                if left_value > value:
                    num_list[index] = left_value
                    num_list[left_index] = left_value
                    max_heapify(num_list, left_index, bar)
                else:
                    return
        else:
            right_value = num_list[right_index]
            if value > left_value:
                if value > right_value:
                    pass
                elif right_value > left_value:
                    num_list[index] = right_value
                    num_list[right_index] = value
                    max_heapify(num_list, right_index, bar)
                else:
                    num_list[index] = left_value
                    num_list[left_index] = value
                    max_heapify(num_list, left_index, bar)

            elif left_value < right_value:
                num_list[index] = right_value
                num_list[right_index] = value
                max_heapify(num_list, right_index, bar)
            else:
                num_list[index] = left_value
                num_list[left_index] = value
                max_heapify(num_list, left_index, bar)
    else:
        if left_value > value:
            num_list[index] = left_value
            num_list[left_index] = value
            max_heapify(num_list, left_index, bar)
        else:
            return


'''
    T(n)=logn
'''


def heapify_increase_key(num_list, index, value):
    if index == 0:
        num_list[index] = value
        return
    parent_index = parent(index)
    parent_value = num_list[parent_index]
    if value > parent_value:
        num_list[index] = parent_value
        num_list[parent_index] = value
        heapify_increase_key(num_list, parent_index, value)
    else:
        return


def heap_extract_max(num_list):
    if len(num_list) == 1:
        return num_list.pop()
    max_value = num_list[0]
    last_index = len(num_list) - 1
    num_list[0] = num_list[last_index]
    num_list.pop()
    max_heapify(num_list, 0, len(num_list) - 1)
    return max_value


def heap_delete(num_list, index):
    heapify_increase_key(num_list, index, maxsize)
    heap_extract_max(num_list)


'''
    T(n)=n
'''


def find_last_root(num_list):
    leaf_start = ceil((len(num_list)) / 2)
    index = leaf_start - 1
    return index


def left(index, num_list):
    res = index * 2 + 1
    if res > len(num_list) - 1:
        return
    else:
        return res


def right(index, num_list):
    res = index * 2 + 2
    if res > len(num_list) - 1:
        return
    return res


def parent(index):
    if index == 0:
        return
    return floor((index - 1) / 2)
