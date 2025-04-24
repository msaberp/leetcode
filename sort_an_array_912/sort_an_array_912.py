from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # base case
        if len(nums) == 1:
            return nums

        # divide
        length = len(nums)
        left_sub_array = self.sortArray(nums[:length // 2])
        right_sub_array = self.sortArray(nums[length // 2:])

        # merge
        left_pointer = 0
        right_pointer = 0
        main_pointer = 0
        while left_pointer < len(left_sub_array) and right_pointer < len(right_sub_array):
            if left_sub_array[left_pointer] < right_sub_array[right_pointer]:
                nums[main_pointer] = left_sub_array[left_pointer]
                left_pointer += 1
            else:
                nums[main_pointer] = right_sub_array[right_pointer]
                right_pointer += 1
            main_pointer += 1
        if left_pointer < len(left_sub_array):
            nums[main_pointer:] = left_sub_array[left_pointer:]
        if right_pointer < len(right_sub_array):
            nums[main_pointer:] = right_sub_array[right_pointer:]
        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 2, 4, 1, 3]
    print(solution.sortArray(nums))
