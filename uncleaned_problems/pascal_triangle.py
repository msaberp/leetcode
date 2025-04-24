from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        list_ = [[1], [1, 1]]
        for row_idx in range(2, numRows):
            row_list = [1]
            for col_idx in range(len(list_[row_idx - 1]) - 1):
                row_list.append(list_[row_idx - 1][col_idx] + list_[row_idx - 1][col_idx + 1])
            row_list.append(1)
            list_.append(row_list)
        return list_


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
