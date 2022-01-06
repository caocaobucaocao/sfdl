from random import randint, seed
from time import time


def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            print('error in {}' % i)
            break
        else:
            continue


seed(time())


def build_random_list():
    num_count = input("sum:")
    min_value: str = input("min value:")
    max_value: str = input("max value:")
    ran_list = []
    for x in range(int(num_count)):
        random_num: int = randint(int(min_value), int(max_value))
        ran_list.append(random_num)
    return ran_list


'''
    T(n)=n
'''


def randomize_in_place(num_list):
    length = len(num_list)
    for x in range(length):
        temp = num_list[x]
        random_value = randint(0, length - 1) % (length - x) + x
        num_list[x] = num_list[random_value]
        num_list[random_value] = temp


def list_remove_duplicate(data):
    res = list()
    for x in range(len(data)):
        if res.count(data[x]) == 0:
            res.append(data[x])
        else:
            pass
    return res
