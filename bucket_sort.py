from random import randrange

'''
If the sum of squares of the sizes of all buckets 
is linear with the total number of elements,Expected run time　Ｔ(n)=O(N)

'''


def bucket_sort(nums):
    length = len(nums)
    buck_list = list()
    for x in range(length):
        buck_list.append(list())
    for x in range(length):
        buck_list[int(nums[x] * 10)].append(nums[x])
    for x in range(len(buck_list)):
        insert_sort(buck_list[x])
    res = list()
    for x in range(length):
        for y in range(len(buck_list[x])):
            res.append(buck_list[x][y])
    return res


def insert_sort(num_list):
    if len(num_list) == 0:
        return None
    elif len(num_list) == 1:
        return num_list
    else:
        for x in range(1, len(num_list), 1):
            for y in range(x, 0, -1):
                value = num_list[y]
                if value >= num_list[y - 1]:
                    break
                else:
                    temp = num_list[y - 1]
                    num_list[y - 1] = value
                    num_list[y] = temp


test_data = list()
for test in range(11):
    test_data.append(randrange(0, 10, 1) / 10)
print(test_data)
print(bucket_sort(test_data))
