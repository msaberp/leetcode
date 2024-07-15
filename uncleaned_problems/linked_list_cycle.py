from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow_pointer = head
        fast_pointer = head
        if slow_pointer.next is None:
            return False
        slow_pointer = slow_pointer.next
        if fast_pointer.next is None or fast_pointer.next.next is None:
            return False
        fast_pointer = fast_pointer.next.next
        while fast_pointer != slow_pointer:
            if slow_pointer.next is None:
                return False
            slow_pointer = slow_pointer.next
            if fast_pointer.next is None or fast_pointer.next.next is None:
                return False
            fast_pointer = fast_pointer.next.next
        return True


if __name__ == '__main__':
    sol = Solution()
    # list_of_int = [3, 2, 0, -4]
    first_node = ListNode(3)
    cycle_node = ListNode(2)
    third_node = ListNode(0)
    forth_node = ListNode(-4)
    first_node.next = cycle_node
    cycle_node.next = third_node
    third_node.next = forth_node
    forth_node.next = cycle_node
    head_ = first_node
    res = sol.hasCycle(head_)
    print(res)
