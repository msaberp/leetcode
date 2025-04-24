# 1530. Number of Good Leaf Nodes Pairs

## Medium

### Topics

### Companies

### Hint

You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

## Example 1

**Input:**
`root = [1,2,3,null,4], distance = 3`

**Output:**
`1`

**Explanation:** The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

## Example 2

**Input:**
`root = [1,2,3,4,5,6,7], distance = 3`

**Output:**
`2`

**Explanation:** The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of the shortest path between them is 4.

## Example 3

**Input:**
`root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3`

**Output:**
`1`

**Explanation:** The only good pair is [2,5].

## Constraints

- The number of nodes in the tree is in the range [1, 2^10].
- 1 <= Node.val <= 100
- 1 <= distance <= 10

## Statistics

- **Accepted:** 79.6K
- **Submissions:** 117.7K
- **Acceptance Rate:** 67.7%

---

## Solution
We use a bottom-up approach. We traverse the tree using the **DFS** algorithm.
While, we don't need to return the good pairs directly, and we only should count them, there is no need to
store the leafs or pairs.

Recursively, traverse the tree until you reach a node, then you return a hashmap which its key is the distance
from that leaf to the current parent node and its value is the number of leafs with that distance.
Therefore, a node will return something like {1: 1}.

For each parent node, first we calculate the hashmap of left sub-tree and then the hashmap of the right sub-tree
and then we loop over all the possible pairs and check if the distance of left plus right sub-trees are less or
equal to the given `distance`. If yes, we add up the `pairs` with value of the left hashmap multiplied with the value
of the right hashmap.

The last part of the code is related to how merge the hashmaps together and increment them and give it to the next
parent in the tree.
On useful optimization here is that during the incrementing phase, we can prune the leafs that are exceeding the given
`distance`. This will speed up the code a lot!

[Link to the NeetCodeIO's YouTube video](https://www.youtube.com/watch?v=f_epkBeS1LQ)