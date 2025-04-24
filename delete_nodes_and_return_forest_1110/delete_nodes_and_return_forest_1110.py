from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, to_delete_list, output_list):
            if not node:
                return None
            node.left = dfs(node.left, to_delete_list, output_list)
            node.right = dfs(node.right, to_delete_list, output_list)

            if node.val in to_delete_list:
                if node.left:
                    output_list.append(node.left)
                if node.right:
                    output_list.append(node.right)
                return None
            else:
                return node

        forest_list = []
        root = dfs(root, to_delete, forest_list)
        if root:
            forest_list.append(root)
        return forest_list


if __name__ == '__main__':
    s = Solution()
    root_ = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))
    res = s.delNodes(root_, [3, 5])
    print(res)



