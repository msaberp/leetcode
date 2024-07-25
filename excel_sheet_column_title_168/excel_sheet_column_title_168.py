class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        columnNumber = columnNumber - 1
        base64 = ""
        while columnNumber >= 0:
            remainder = columnNumber % 26
            base64 = alphabet[remainder] + base64
            columnNumber //= 26
            columnNumber = columnNumber - 1
        return base64


if __name__ == "__main__":
    s = Solution()
    columnNumber = 1
    print(s.convertToTitle(columnNumber))
