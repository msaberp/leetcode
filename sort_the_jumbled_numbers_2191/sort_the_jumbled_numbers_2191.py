from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def func_mapping(num: int) -> int:
            mapped_num = ""
            for digit in str(num):
                mapped_num += str(mapping[int(digit)])
            return int(mapped_num)

        res = sorted(nums, key=lambda x: func_mapping(x))
        return res


if __name__ == '__main__':
    solution = Solution()
    mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    nums = [991, 388, 38]
    print(solution.sortJumbled(mapping, nums))
