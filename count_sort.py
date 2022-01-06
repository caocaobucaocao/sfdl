"""
    T(n)=n+k,k=max(num_list),when k<O(n) ,pick this
"""


def counting_sort(num_list):
    if len(num_list) == 0:
        return None
    elif len(num_list) == 1:
        return num_list
    else:
        res = [0 for x in range(len(num_list))]
        temps = [0 for x in range(max(num_list) + 1)]
        for x in range(len(num_list)):
            temps[num_list[x]] = temps[num_list[x]] + 1
        for x in range(1, len(temps), 1):
            temps[x] = temps[x] + temps[x - 1]
        for x in range(len(num_list) - 1, -1, -1):
            res[temps[num_list[x]] - 1] = num_list[x]
            temps[num_list[x]] = temps[num_list[x]] - 1
        return res

#
# list = build_random_list()
# res1 = counting_sort(list)
# print(res1)
# is_sorted(res1)
