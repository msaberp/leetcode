from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_: List[int] = []
        stack_: List[TreeNode] = []

        current_node = root
        while current_node or stack_:
            while current_node:
                stack_.append(current_node)
                current_node = current_node.left
            current_node = stack_.pop()
            list_.append(current_node.val)
            current_node = current_node.right
        return list_


if __name__ == "__main__":
    print("Solution is started ...")
    root_ = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3), right=None))
    # root_ = TreeNode(1)
    solution = Solution()
    res = solution.inorderTraversal(root_)
    print("solution is", res)
    print("Solution is finished ...")

