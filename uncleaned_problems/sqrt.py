class Solution:
    def mySqrt(self, x: int) -> int:
        # root = 0
        # while root * root <= x:
        #     root += 1
        # return root - 1
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high


if __name__ == '__main__':
    import cProfile
    num = 110
    # cProfile.run('Solution().mySqrt(num)')
    s = Solution()
    print(s.mySqrt(num))