import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]+', '', s)
        s = s.lower()
        lower_pointer = 0
        upper_pointer = len(s) - 1
        while lower_pointer < upper_pointer:
            if s[lower_pointer] == s[upper_pointer]:
                lower_pointer += 1
                upper_pointer -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    string = "ab_a"
    print(solution.isPalindrome(string))