import numpy as numpy
import random


class ClsByAry:
    def __init__(self, cls_count):
        super().__init__()
        self.cls_list = numpy.zeros([cls_count, 3], dtype=int)
        self.root = random.randint(0, cls_count - 1)
        self.tail = self.root

    def insert(self, key, index):
        if self.cls_list[1][index] == 0:
            pass


print(ClsByAry(17).cls_list)
