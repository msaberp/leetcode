from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num_idx, num in enumerate(nums):
            tmp = nums.copy()
            tmp.pop(num_idx)
            if num in tmp:
                continue
            else:
                return num


if __name__ == '__main__':
    sol = Solution()
    nums_ = [1, 0, 1]
    print(sol.singleNumber(nums_))