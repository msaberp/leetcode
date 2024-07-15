class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_sub_string(substring: str, point: int) -> int:
            nonlocal s
            total_score = 0
            stack_ = []
            for char_ in s:
                if not stack_:
                    stack_.append(char_)
                    continue
                top = stack_[-1]
                if top + char_ == substring:
                    total_score += point
                    stack_.pop()
                else:
                    stack_.append(char_)
            s = ''.join(stack_)
            return total_score

        res = 0
        if x > y:
            res += remove_sub_string("ab", x)
            res += remove_sub_string("ba", y)
        else:
            res += remove_sub_string("ba", y)
            res += remove_sub_string("ab", x)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maximumGain("cdbcbbaaabab", 4, 5))