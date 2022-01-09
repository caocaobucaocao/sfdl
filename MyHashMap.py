import random
from math import log2, ceil, sqrt
import numpy


class MyHashMap:
    def __init__(self, element_count):
        super(MyHashMap, self).__init__()
        n = ceil(log2(element_count))
        self.size = 2 ** n
        self.bucket = self.find_bucket()
        self.load_factor = int(self.size / self.bucket)
        self.data = numpy.ones((self.bucket, int(self.load_factor)), numpy.uint8, ) * -1

    def __hash__(self, key):
        return key % self.bucket

    def find_bucket(self):
        for x in range(self.size, 3, -1):
            stop = ceil(sqrt(self.size))
            is_pr = True
            for y in range(5, stop, 6):
                if self.size % y == 0 or self.size % (y + 2) == 0:
                    is_pr and False
                else:
                    pass
            if is_pr:
                return y

    def __str__(self):
        return "{},{},{},{}".format(self.size, self.bucket, self.load_factor, self.data)


test = MyHashMap(random.randint(10, 2047))
print(test)
