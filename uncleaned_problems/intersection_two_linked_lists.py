from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer_a = headA
        pointer_b = headB
        counter = 0

        # find the correct padding between first and second linked lists using counter variable
        while pointer_a is not None:
            pointer_a = pointer_a.next
            counter += 1
        while pointer_b is not None:
            pointer_b = pointer_b.next
            counter -= 1

        # resetting the pointer
        pointer_a = headA
        pointer_b = headB

        # if counter is negative move `pointer_b` forward, otherwise move `pointer_a` forward
        if counter > 0:
            while counter > 0:
                pointer_a = pointer_a.next
                counter -= 1
        else:
            while counter < 0:
                pointer_b = pointer_b.next
                counter += 1

        # now both pointers are pointing at the same level of linked list
        # we move forward until we find the intersection
        intersection = None
        while pointer_a is not None and pointer_b is not None:
            if pointer_a == pointer_b:
                intersection = pointer_a
                break
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
        return intersection


def convert_list_to_linked_list(input_list: list) -> Optional[ListNode]:
    if len(input_list) == 0:
        return None

    node = None
    next_node = ListNode(input_list.pop())
    while input_list:
        node = ListNode(input_list.pop())
        node.next = next_node
        next_node = node
    return node


if __name__ == '__main__':
    list_a = [4, 1, 8, 4, 5]
    list_b = [5, 6, 1, 8, 4, 5]
    head_a = convert_list_to_linked_list(list_a)
    head_b = convert_list_to_linked_list(list_b)
    sol = Solution()
    res = sol.getIntersectionNode(head_a, head_b)
    print(res)