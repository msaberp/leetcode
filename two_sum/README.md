# Two Sum (LeetCode #1)

## Table of Contents
- [Problem Description](#problem-description)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solution Approaches](#solution-approaches)
  - [Brute Force Approach](#brute-force-approach)
  - [Hash Map Approach](#hash-map-approach)

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

## Solution Approaches

### Brute Force Approach

**Algorithm:**
- Use two nested loops to check every possible pair of numbers in the array.
- For each pair, check if they sum up to the target.

**Time Complexity:** O(n²) - where n is the length of the array.  
**Space Complexity:** O(1) - no extra space required.

### Hash Map Approach

**Algorithm:**
- Create a hash map to store array elements and their indices.
- Iterate through the array once:
  - For each element, check if `target - current_element` exists in the hash map.
  - If it exists, return the current index and the index stored in the hash map.
  - Otherwise, add the current element and its index to the hash map.

**Time Complexity:** O(n) - where n is the length of the array.  
**Space Complexity:** O(n) - for storing the hash map.

This approach is optimal for the problem as it achieves O(n) time complexity, satisfying the follow-up question that asks for a solution better than O(n²).

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?