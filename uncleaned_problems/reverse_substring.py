class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack_ = []
        str_idx = 0
        while str_idx < len(s):
            if s[str_idx] == ')':
                rev_str = ""
                top_char = stack_.pop()
                while top_char != '(':
                    rev_str += top_char
                    top_char = stack_.pop()
                for char_ in rev_str:
                    stack_.append(char_)
                str_idx += 1
            else:
                stack_.append(s[str_idx])
                str_idx += 1
        return ''.join(stack_)


if __name__ == '__main__':
    s = Solution()
    string = "(u(love)i)"
    print(s.reverseParentheses(string))