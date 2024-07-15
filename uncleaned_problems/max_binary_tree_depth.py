from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        max_depth = 0
        depth = 0
        stack_: List[(TreeNode, int)] = []

        current_node = root
        while current_node or stack_:
            if current_node is None:
                current_node, depth = stack_.pop()
                current_node = current_node.right
            else:
                depth += 1
                stack_.append((current_node, depth))
                current_node = current_node.left
                if max_depth < depth:
                    max_depth = depth

        return max_depth


if __name__ == "__main__":
    print("Solution is started ...")
    root_ = TreeNode(val=3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    solution = Solution()
    res = solution.maxDepth(root_)
    print("solution is", res)
    print("Solution is finished ...")

