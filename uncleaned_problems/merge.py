from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_last_idx = m - 1
        nums2_last_idx = n - 1
        insertion_idx = m + n - 1

        while nums1_last_idx >= 0 and nums2_last_idx >= 0:
            if nums1[nums1_last_idx] > nums2[nums2_last_idx]:
                nums1[insertion_idx] = nums1[nums1_last_idx]
                insertion_idx -= 1
                nums1_last_idx -= 1
            else:
                nums1[insertion_idx] = nums2[nums2_last_idx]
                insertion_idx -= 1
                nums2_last_idx -= 1

        while nums2_last_idx >= 0:
            nums1[insertion_idx] = nums2[nums2_last_idx]
            insertion_idx -= 1
            nums2_last_idx -= 1


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 3, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)
