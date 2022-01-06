from test_util import build_random_list, is_sorted
from math import floor
from random import randint


def quick_sort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        quick_sort(nums, p, q - 1)
        quick_sort(nums, q + 1, r)
    else:
        return


def partition(nums, p, r):
    # random zhu yuan
    exchange_index = randint(p, r)
    x = nums[r]
    nums[r] = nums[exchange_index]
    nums[exchange_index] = x
    x = nums[r]
    i = p - 1
    count = 0
    for j in range(p, r):
        if nums[j] == x:
            count = count + 1
        if nums[j] < x:
            i = i + 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        else:
            pass
    if count == r - p:
        return floor((r - p) / 2)
    else:
        temp = nums[i + 1]
        nums[i + 1] = nums[r]
        nums[r] = temp
        return i + 1

# test
# num_list = build_random_list()
# quick_sort(num_list, 0, len(num_list) - 1)
# print(num_list)
# is_sorted(num_list)
# for index in range(len(num_list)):
#     num_list[index] = 5
# print(num_list)
# print(partition(num_list, 0, len(num_list) - 1))
