from heap import heapify_increase_key


def increase_key(num_list, x: int, key: int):
    index = num_list.index(x)
    heapify_increase_key(num_list, index, key)


def insert_key(num_list, key):
    num_list.append(key)
    heapify_increase_key(num_list, len(num_list) - 1, key)


def maximum_value(num_list):
    if len(num_list):
        return num_list[0]
