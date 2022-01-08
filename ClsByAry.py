import numpy as numpy


class ClsByAry:
    def __init__(self, cls_size):
        super().__init__()
        self.vessel = numpy.ones((cls_size, 3), numpy.uint8, ) * -1
        self.capacity = cls_size
        self.cls_size = cls_size
        self.cls_list = 0
        self.free = 1

    def allocate_object(self):
        if self.full():
            return False
        else:
            self.capacity = self.capacity - 1
            res = self.free
            self.free = self.vessel[0][self.free]
            self.vessel[2][self.cls_list] = res
            self.vessel[0][res] = self.cls_list
            self.cls_list = res
            return res

    def free_object(self, index):
        if self.empty():
            return False
        else:
            self.capacity = self.capacity + 1
            index_next = self.vessel[0][index]
            index_prev = self.vessel[2][index]
            self.vessel[0][index_prev] = index_next
            self.vessel[2][index_next] = index_prev
            self.vessel[0][index] = self.free
            self.free = index
            return True

    def empty(self):
        if self.capacity == self.cls_size:
            return True
        else:
            return False

    def full(self):
        if self.capacity == 0:
            return True
        else:
            return False


print(ClsByAry(17).vessel)
