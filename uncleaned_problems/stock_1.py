from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        left_pointer = 0
        right_pointer = 1
        profit = 0
        while right_pointer < len(prices):
            if profit < prices[right_pointer] - prices[left_pointer]:
                profit = prices[right_pointer] - prices[left_pointer]
            if prices[right_pointer] < prices[left_pointer]:
                left_pointer += 1
                right_pointer = left_pointer + 1
            else:
                right_pointer += 1
        return profit


if __name__ == "__main__":
    sol = Solution()
    prices = [7,6,4,3,1]
    res = sol.maxProfit(prices)
    print(res)
