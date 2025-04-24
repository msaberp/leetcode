class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        player_idx = 0
        for i in range(1, n):
            player_idx += k
            player_idx %= (i + 1)
        return player_idx + 1


if __name__ == '__main__':
    sol = Solution()
    n = 5
    k = 2
    res = sol.findTheWinner(n, k)
    print(res)