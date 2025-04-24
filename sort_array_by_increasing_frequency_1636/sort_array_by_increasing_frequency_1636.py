from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        sorted_list = sorted(counter.items(), key=lambda x: (x[1], -x[0]))
        res_list = []
        for key, val in sorted_list:
            res_list.extend([key] * val)
        return res_list


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 2, 3]
    print(s.frequencySort(nums))
