import array
import random


def radix_sort(nums, b, r):
    """
        T(n)=(d/r)*C(n),C(n)=n+k,k=2**r
    :param nums:data
    :param b:digit
    :param r:split digit
    :return:sorted list
    """
    nums_list = list()
    d_sum = int(b / r)
    for x in range(len(nums)):
        bin_str = bin(nums[x])
        start = 2
        end = r + 2
        res = list()
        for y in range(d_sum):
            temp = int(bin_str[start + y * r:end + y * r], 2)
            res.append(temp)
        print(res)
        nums_list.append(res)

    r_digit_max = 2 ** r
    for x in range(d_sum - 1, -1, -1):
        nums_list = counting_sort(nums_list, x, r_digit_max)
    res = list()
    for x in range(len(nums)):
        sum_item = 0
        for y in range(d_sum):
            sum_item = sum_item + nums_list[x][y] * (4 ** (d_sum - y - 1))
        res.append(sum_item)
    return res


"""
    T(n)=n+k,k=max(num_list),when k<O(n) ,pick this
"""


def counting_sort(nums_list, d, max_value):
    if len(nums_list) == 0:
        return None
    elif len(nums_list) == 1:
        return nums_list
    else:
        res = [0 for x in range(len(nums_list))]
        temps = [0 for x in range(max_value)]
        for x in range(len(nums_list)):
            temps[nums_list[x][d]] = temps[nums_list[x][d]] + 1

        for x in range(1, len(temps), 1):
            temps[x] = temps[x] + temps[x - 1]

        for x in range(len(nums_list) - 1, -1, -1):
            res[temps[nums_list[x][d]] - 1] = nums_list[x]
            temps[nums_list[x][d]] = temps[nums_list[x][d]] - 1
            pass
        return res


'''
 test
'''
# a = array.array("I", [random.randint(128, 255) for x in range(9)])
# print(a.tolist())
# for x in range(len(a)):
#     print(bin(a[x]))
#
# print(radix_sort(a, 8, 2))
