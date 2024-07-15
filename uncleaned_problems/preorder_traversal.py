from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(node: Optional[TreeNode], visited_nodes: List[int]):
            if node is None:
                return
            visited_nodes.append(node.val)
            traversal(node.left, visited_nodes)
            traversal(node.right, visited_nodes)
        list_ = []
        traversal(root, list_)
        return list_


if __name__ == "__main__":
    root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    solution = Solution()
    res = solution.preorderTraversal(root)
    print(res)
