from random import randint, seed, random
from time import time
from math import sqrt, ceil


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


def is_primer(num):
    if num == 0 or num == 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 6 != 1 and num % 6 != 5:
        return False
    else:
        stop = ceil(sqrt(num))
        for x in range(5, stop, 6):
            if num % x == 0 or num % (x + 2) == 0:
                return False
            else:
                pass
        return True


a = int(random() * 100)
print(a)
print(is_primer(a))
