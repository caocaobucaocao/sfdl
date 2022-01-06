import numpy as np
from numpy import int8, uint8


class YongMatrix:

    def extract_min(self):
        if self.empty():
            return None
        else:
            temp = self.data[0][0]
            self.node_descend(row=0, col=0)
            return temp

    def contain(self, value):
        col = self.width - 1
        row = 0
        for x in range(self.width + self.deep - 1):
            if col < 0 or row > self.deep - 1:
                return -1, -1
            else:
                if value > self.data[row][col]:
                    row = row + 1
                elif value < self.data[row][col]:
                    col = col - 1
                else:
                    return row, col

    def node_descend(self, **index):
        row = index.get('row')
        col = index.get('col')
        value = self.data[row][col]
        if col < self.width - 1:
            right_value = self.data[row][col + 1]
            if row < self.deep - 1:
                bottom_value = self.data[row + 1][col]
                if value < right_value and value < bottom_value:
                    return
                elif right_value < value and right_value < bottom_value:
                    self.data[row][col] = right_value
                    self.data[row][col + 1] = value
                    col = col + 1
                    self.node_descend(row=row, col=col)
                else:
                    self.data[row + 1][col] = self.data[row][col]
                    self.data[row][col] = bottom_value
                    row = row + 1
                    self.node_descend(row=row, col=col)
            else:
                if value < right_value:
                    return
                else:
                    self.data[row][col] = right_value
                    self.data[row][col + 1] = value
                    col = col + 1
                    self.node_descend(row=row, col=col)
            return
        else:
            if row < self.deep - 1:
                bottom_value = self.data[row + 1][col]
                if value < bottom_value:
                    return
                else:
                    self.data[row + 1][col] = value
                    self.data[row][col] = bottom_value
                    row = row + 1
                    self.node_descend(row=row, col=col)
            else:
                return

    def __init__(self, width, deep):
        super().__init__()
        self.width = width
        self.deep = deep
        # 255==-infinite,0-254 
        self.data = np.ones((width, deep), uint8, ) * 255

    def empty(self):
        if self.data[0][0] == 255:
            return True
        else:
            return False

    def full(self):
        if self.data[self.deep - 1][self.width - 1] == 255:
            return False
        else:
            return True


yong = YongMatrix(5, 6)
print(yong.data)
yong.data[0][0] = 258
print(yong.data)
