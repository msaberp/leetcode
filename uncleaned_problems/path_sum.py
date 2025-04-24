from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        if root.left:
            left_res = self.hasPathSum(root.left, targetSum - root.val)
            if left_res:
                return True
        if root.right:
            right_res = self.hasPathSum(root.right, targetSum - root.val)
            if right_res:
                return True

        return False


if __name__ == '__main__':
    root = TreeNode(1)
    root_2 = TreeNode(5, left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))), right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1))))
    root_3 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    solution = Solution()
    res = solution.hasPathSum(root_3, 5)
    print(res)
