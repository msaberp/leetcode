from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0

        def dfs(node):
            if not node:
                return defaultdict(int)
            if not node.left and not node.right:
                counter = defaultdict(int)
                counter[1] = 1
                return counter

            left_dists = dfs(node.left)
            right_dists = dfs(node.right)

            for left_dist in left_dists:
                for right_dist in right_dists:
                    if left_dist + right_dist <= distance:
                        self.pairs += left_dists[left_dist] * right_dists[right_dist]

            all_dists = defaultdict(int)
            for left_dist in left_dists:
                if left_dist + 1 < distance:
                    all_dists[left_dist + 1] += left_dists[left_dist]
            for right_dist in right_dists:
                if right_dist + 1 < distance:
                    all_dists[right_dist + 1] += right_dists[right_dist]
            return all_dists

        dfs(root)
        return self.pairs


if __name__ == '__main__':
    sol = Solution()
    root_ = TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3))
    distance_ = 3
    res = sol.countPairs(root_, distance_)
    print(res)