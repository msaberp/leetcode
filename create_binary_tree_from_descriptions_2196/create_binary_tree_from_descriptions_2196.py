from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree_node_dict = {}
        children = set()
        for parent, child, is_left in descriptions:
            children.add(child)
            if parent not in tree_node_dict:
                tree_node_dict[parent] = TreeNode(parent)
            if child not in tree_node_dict:
                tree_node_dict[child] = TreeNode(child)
            if is_left:
                tree_node_dict[parent].left = tree_node_dict[child]
            else:
                tree_node_dict[parent].right = tree_node_dict[child]

        for node in tree_node_dict:
            if node not in children:
                return tree_node_dict[node]
        return


if __name__ == '__main__':
    solution = Solution()
    descriptions_ = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    result = solution.createBinaryTree(descriptions_)
    print(result)
