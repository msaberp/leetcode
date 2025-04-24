from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True

        stack_left: List[TreeNode] = []
        stack_right: List[TreeNode] = []

        left_node = root.left
        right_node = root.right
        while left_node or right_node or stack_left or stack_right:
            if bool(left_node) != bool(right_node):
                return False
            if left_node is None and right_node is None:
                left_node = stack_left.pop()
                left_node = left_node.right
                right_node = stack_right.pop()
                right_node = right_node.left
            else:
                if left_node.val != right_node.val:
                    return False
                stack_left.append(left_node)
                stack_right.append(right_node)
                left_node = left_node.left
                right_node = right_node.right
        return True


if __name__ == "__main__":
    print("Solution is started ...")
    root_ = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(val=2, left=TreeNode(4), right=TreeNode(3)))
    solution = Solution()
    res = solution.isSymmetric(root_)
    print("solution is", res)
    print("Solution is finished ...")

