from quick_sort import partition
import test_util


def randomized_select(data, p, r, i):
    if p == r:
        return data[p]
    else:
        q = partition(data, p, r)
        k = q - p + 1
        if i == k:
            return data[q]
        elif i < k:
            randomized_select(data, p, q, i)
        else:
            randomized_select(data, q + 1, r, i - k)


nums = test_util.build_random_list()
nums = test_util.list_remove_duplicate(nums)

print(nums)
