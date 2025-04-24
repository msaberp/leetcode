from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack_of_directories = []
        for operation in logs:
            if operation == "./":
                continue
            elif operation == "../":
                if len(stack_of_directories) == 0:
                    continue
                stack_of_directories.pop()
            else:
                stack_of_directories.append(operation)
        return len(stack_of_directories)


if __name__ == "__main__":
    sol = Solution()
    logs_ = ["d1/", "d2/", "../", "d21/", "./"]
    print(sol.minOperations(logs_))
