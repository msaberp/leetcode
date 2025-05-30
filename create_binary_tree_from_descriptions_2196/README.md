# 2196. Create Binary Tree From Descriptions

### [Medium]

## Description

You are given a 2D integer array `descriptions` where `descriptions[i] = [parenti, childi, isLefti]` indicates that `parenti` is the parent of `childi` in a binary tree of unique values. Furthermore:

- If `isLefti == 1`, then `childi` is the left child of `parenti`.
- If `isLefti == 0`, then `childi` is the right child of `parenti`.

Construct the binary tree described by `descriptions` and return its root.

The test cases will be generated such that the binary tree is valid.

## Examples

### Example 1

Input: `descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]`

Output: `[50,20,80,15,17,19]`

Explanation: The root node is the node with value 50 since it has no parent. The resulting binary tree is shown in the diagram.

### Example 2

Input: `descriptions = [[1,2,1],[2,3,0],[3,4,1]]`

Output: `[1,2,null,null,3,4]`

Explanation: The root node is the node with value 1 since it has no parent. The resulting binary tree is shown in the diagram.

## Constraints

- `1 <= descriptions.length <= 10^4`
- `descriptions[i].length == 3`
- `1 <= parenti, childi <= 10^5`
- `0 <= isLefti <= 1`
- The binary tree described by `descriptions` is valid.

## Submission Stats

- Accepted: 69.7K
- Submissions: 88.7K
- Acceptance Rate: 78.6%

---

## Solution

We use a hash map (Python dictionary) which will store a tree (sub-tree) for a given key which is the sub-tree's root's value.

We iterate over the description list, if the parent or child is already in the hash map, we will use it, otherwise we will create a new sub-tree.

This approach will create the tree step by step. On each step, we are creating one edge of the graph.
However, this will not give us the root of the tree.

In order to keep track of which node is the root, we keep track of the child nodes. To do that, we use a set to store all seen children.

In the end, we iterate over the keys of the hash map and whatever node that is not seen as a child node, it is the root of the tree.

[NeetCodeIO's Youtube link](https://www.youtube.com/watch?v=yWkrFfqO7NA)