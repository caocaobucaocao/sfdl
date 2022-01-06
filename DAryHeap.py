from math import ceil, log, floor
from sys import maxsize


class DAryHeap:

    def build_max_d_heap_by_insert(self):
        for x in range(len(self.num_list)):
            self.max_heap_insert(x, self.num_list[x])

    def max_heap_insert(self, index, value):
        if index == 0:
            self.num_list[0] = value
        self.heap_increase_value(index, value)

    def heap_increase_value(self, index, value):
        if value < self.num_list[index]:
            return
        else:
            self.num_list[index] = value
            parent_index = self.parent(index)
            if parent_index is None:
                return
            else:
                parent_value = self.num_list[parent_index]
                if parent_value > value:
                    return
                else:
                    self.heap_increase_value(parent_index, value)

    def build_max_d_heap(self):
        for x in range(self.last_root_index, -1, -1):
            self.max_heapify(x)

    def max_heapify(self, index):
        child_index_list = self.find_child(index)
        max_value = self.num_list[index]
        max_value_index = index
        for x in child_index_list:
            value = self.num_list[x]
            if value > max_value:
                max_value = value
                max_value_index = x
            else:
                pass
        if index == max_value_index:
            return
        else:
            temp = self.num_list[index]
            self.num_list[index] = max_value
            self.num_list[max_value_index] = temp
            self.max_heapify(max_value_index)

    def maximum(self):
        return self.num_list[0]

    def extract_max(self):
        if self.num_list:
            return
        temp = self.num_list[0]
        self.num_list[0] = self.num_list[len(self.num_list) - 1]
        self.num_list.pop(len(self.num_list) - 1)
        self.last_root_index = floor(len(self.num_list) / self.ary) - 1
        self.max_heapify(0)
        return temp

    def heap_delete(self, index):
        if index < len(self.num_list):
            value = self.num_list[index]
            self.heap_increase_value(index, maxsize)
            self.extract_max()
            return value
        else:
            return None

    def parent(self, index):
        if index > self.ary:
            return ceil(index / self.ary - 1)
        elif index == 0:
            pass
        else:
            return 0

    def find_child(self, index):
        child_index_list = list()
        if index > self.last_root_index:
            return child_index_list
        child_start_index = (index + 1) * self.ary + (2 * self.ary - self.ary ** 2 - 1) / (self.ary - 1)
        child_start_index = int(child_start_index)
        if len(self.num_list) - 1 < child_start_index + self.ary - 1:
            child_index_end = len(self.num_list) - 1
        else:
            child_index_end = child_start_index + self.ary - 1
        for x in range(child_start_index, child_index_end + 1):
            child_index_list.append(x)
        return child_index_list

    def floor_index(self, index):
        return ceil(log((self.ary - 1) * (index + 1), self.ary))

    def __init__(self, nums, ary):
        super().__init__()
        self.ary = ary
        self.height = ceil(log((ary - 1) * len(nums), ary))
        self.num_list = list(nums)
        if len(self.num_list) >= self.ary:
            self.last_root_index = floor(len(self.num_list) / self.ary) - 1
        elif len(self.num_list) == 1:
            self.last_root_index = None
        else:
            self.last_root_index = 0

    def __str__(self):
        res = ' height= {},ary= {}, length={},nums= {} ,last_index={} ,last_root_index={}' \
            .format(self.height, self.ary, len(self.num_list), self.num_list, len(self.num_list) - 1,
                    self.last_root_index)
        return res

    def d_heap_check(self):
        res = True
        if not self.num_list:
            return res
        for x in range(self.last_root_index + 1, -1, -1):
            child_index_list = self.find_child(x)
            for y in child_index_list:
                res = res and (self.num_list[x] >= self.num_list[y])
                if not res:
                    print('x=%d,value=%d' % (x, self.num_list[x]))
                    print('y=%d,value=%d' % (y, self.num_list[y]))
                    return res
                else:
                    pass
        return res
