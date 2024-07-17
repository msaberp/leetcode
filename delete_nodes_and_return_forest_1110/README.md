# 1110. Delete Nodes And Return Forest

## Medium

### Topics

### Companies

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

## Example 1

**Input:**
`root = [1,2,3,4,5,6,7], to_delete = [3,5]`

**Output:**
`[[1,2,null,4],[6],[7]]`


## Example 2

**Input:**
`root = [1,2,4,null,3], to_delete = [3]`

**Output:**
`[[1,2,4]]`


## Constraints

- The number of nodes in the given tree is at most 1000.
- Each node has a distinct value between 1 and 1000.
- `to_delete.length` <= 1000
- `to_delete` contains distinct values between 1 and 1000.

## Statistics

- **Accepted:** 262.6K
- **Submissions:** 373.2K
- **Acceptance Rate:** 70.3%

---

## Solution
In order to solve this problem, we have to split it into two sub-problems:
- deleting nodes
- collecting tree roots

For deletion step, we need a bottom-up approach which each node, will report to its parent if it is deleted or not.
In case of deletion the DFS traverse function will return `None`, otherwise it returns the node.

During the deletion process, we can keep track of newly generated tree roots. If a node is going to be deleted, we can
add its children to a list.
At the end, if the old root is still valid (it is not deleted) we also add it in the list and return the list.