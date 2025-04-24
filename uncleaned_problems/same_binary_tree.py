from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p: List[TreeNode] = []
        stack_q: List[TreeNode] = []

        while p or q or stack_p or stack_q:
            if bool(p) != bool(q):
                return False
            if p is None and q is None:
                p = stack_p.pop()
                p = p.right
                q = stack_q.pop()
                q = q.right
            else:
                if p.val != q.val:
                    return False
                stack_p.append(p)
                stack_q.append(q)
                p = p.left
                q = q.left

        return True


if __name__ == "__main__":
    tree1 = TreeNode(1, left=TreeNode(2), right=TreeNode(2))
    tree2 = TreeNode(1, left=TreeNode(2), right=TreeNode(2))
    sol = Solution()
    res = sol.isSameTree(tree1, tree2)
    print(res)
