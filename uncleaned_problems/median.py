from typing import List


class SortedList:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.median_index = None

    def __len__(self):
        return len(self.nums)

    def __getitem__(self, item):
        return self.nums[item]

    def __repr__(self):
        return f"list: {self.nums}, median_index: {self.median_index}"


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums1 = SortedList(nums1)
        nums2 = SortedList(nums2)
        self.find_median_indices(nums1, nums2)
        max_left = self.find_max_left(nums1, nums2)
        min_right = self.find_min_right(nums1, nums2)

        if (len(nums1) + len(nums2)) % 2 == 1:
            return float(max_left)
        return (max_left + min_right) / 2

    def find_median_indices(self, nums1: SortedList, nums2: SortedList) -> None:
        index_min, index_max = 0, len(nums1)
        half_length = (len(nums1) + len(nums2) + 1) // 2

        while index_min <= index_max:
            nums1.median_index = (index_min + index_max) // 2
            nums2.median_index = half_length - nums1.median_index

            if nums1.median_index < len(nums1) and nums1[nums1.median_index] < nums2[nums2.median_index - 1]:
                index_min += 1
            elif nums1.median_index > 0 and nums1[nums1.median_index - 1] > nums2[nums2.median_index]:
                index_max -= 1
            else:
                break

    def find_max_left(self, nums1: SortedList, nums2: SortedList) -> int:
        if nums1.median_index == 0:
            return nums2[nums2.median_index - 1]
        elif nums2.median_index == 0:
            return nums1[nums1.median_index - 1]
        return max(nums1[nums1.median_index - 1], nums2[nums2.median_index - 1])

    def find_min_right(self, nums1: SortedList, nums2: SortedList) -> int:
        if nums1.median_index == len(nums1):
            return nums2[nums2.median_index]
        elif nums2.median_index == len(nums2):
            return nums1[nums1.median_index]
        return min(nums1[nums1.median_index], nums2[nums2.median_index])


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([], [2]))