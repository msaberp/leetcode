from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_in_rows = {min(row) for row in matrix}
        max_in_cols = {max(col) for col in zip(*matrix)}
        return list(min_in_rows & max_in_cols)


if __name__ == '__main__':
    sol = Solution()
    print(sol.luckyNumbers([[1, 2, 3], [4, 5, 6]]))
