from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        while current_node:
            current_node.next = self.get_next_node(current_node)
            current_node = current_node.next
        return head

    def get_next_node(self, node: Optional[ListNode]) -> Optional[ListNode]:
        while node and node.next and node.val == node.next.val:
            node = node.next
        return node.next


if __name__ == "__main__":
    s = Solution()
    head_ = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print(s.deleteDuplicates(head_))