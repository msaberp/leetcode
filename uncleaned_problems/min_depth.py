from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)
        if left_depth == 0 and right_depth == 0:
            min_depth = 1
        elif left_depth == 0:
            min_depth = 1 + right_depth
        elif right_depth == 0:
            min_depth = 1 + left_depth
        else:
            min_depth = 1 + min(left_depth, right_depth)
        return min_depth


if __name__ == "__main__":
    solution = Solution()
    root_ = TreeNode(1)
    res = solution.minDepth(root_)
    print(res)
