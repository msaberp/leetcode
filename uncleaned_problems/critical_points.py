from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        list_ = []
        node = self
        while node is not None:
            list_.append(node.val)
            node = node.next
        return str(list_)


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        length_list = [-1, -1]
        prev_node = None
        min_length = float('inf')
        max_length = 0
        first_critical_point = True
        start_counting = False
        # critical_node_pointer = None
        dist = 0
        while head is not None:
            if self.is_critical_point(head, prev_node):
                if first_critical_point:
                    # critical_node_pointer = head
                    first_critical_point = False
                    start_counting = True
                else:
                    if dist < min_length:
                        min_length = dist
                    max_length = max_length + dist
                    dist = 0
            prev_node = head
            head = head.next
            if start_counting:
                dist += 1
        if min_length < float('inf') and max_length > 0:
            length_list = [min_length, max_length]
        return length_list

    def is_critical_point(self, head: ListNode, prev_node: Optional[ListNode]) -> bool:
        if prev_node is None:
            return False
        if head.next is None:
            return False
        if prev_node.val < head.val and head.val > head.next.val:
            return True
        if prev_node.val > head.val and head.val < head.next.val:
            return True
        return False


def convert_into_linked_list(list_of_int: List[int]) -> Optional[ListNode]:
    if len(list_of_int) == 0:
        return None
    head_ = ListNode()
    tmp = head_
    for num_idx in range(len(list_of_int) - 1):
        tmp.val = list_of_int[num_idx]
        tmp.next = ListNode()
        tmp = tmp.next
    tmp.val = list_of_int[-1]
    return head_


if __name__ == '__main__':
    solution = Solution()
    linked_list = convert_into_linked_list([3,1])
    res = solution.nodesBetweenCriticalPoints(linked_list)
    print(res)