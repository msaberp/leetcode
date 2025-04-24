import math
from typing import List


class Point:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
        self.start = x
    
    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def move(self, direction) -> str:
        if direction == 'r':
            if self.y == self.n - 1:
                direction = 'd'
                self.move(direction)
            else:
                self.y = self.y + 1
        elif direction == 'd':
            if self.x == self.n - 1:
                direction = 'l'
                self.move(direction)
            else:
                self.x = self.x + 1
        elif direction == 'l':
            if self.y == self.start:
                direction = 'u'
                self.move(direction)
            else:
                self.y = self.y - 1
        elif direction == 'u':
            if self.x == self.start:
                direction = 'r'
                self.move(direction)
            else:
                self.x = self.x - 1
        else:
            raise Exception("The direction is not defined")
        
        return direction
    
def rotate_layer(start, end, matrix):
    if end - start == 1:
        return
    
    point = Point(start, start, end)
    direction = 'r'
    flat_mat = []

    # spinning around the matrix and save numbers in a list
    while not (point == Point(start, start, end) and direction == 'u'):
        flat_mat.append(matrix[point.x][point.y])
        direction = point.move(direction)

    # shift to right
    for _ in range(end - start - 1):
        flat_mat.insert(0, flat_mat.pop())

    # rotating the matrix
    point = Point(start, start, end)
    direction = 'r'
    while not (point == Point(start, start, end) and direction == 'u'):
        matrix[point.x][point.y] = flat_mat.pop(0)
        direction = point.move(direction)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1:
            return
        
        n = len(matrix)
        layers = math.ceil(n // 2)
        
        for layer_idx in range(layers):
            rotate_layer(layer_idx, n, matrix)
            n -= 1
        

if __name__ == "__main__":
    _input = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution = Solution()
    solution.rotate(_input)
    print(_input)