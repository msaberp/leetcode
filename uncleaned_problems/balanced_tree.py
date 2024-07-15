from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]

    def dfs(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if root is None:
            return True, 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return balanced, 1 + max(left[1], right[1])


if __name__ == "__main__":
    solution = Solution()
    tree_1 = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    tree_2 = TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)), right=TreeNode(2))
    # [1,2,2,3,null,null,3,4,null,null,4]
    res = solution.isBalanced(tree_2)
    print(res)
