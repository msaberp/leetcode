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
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        sum_ = 0
        start_sum = False
        prev_sum_node = head
        while tmp is not None:
            if tmp.val == 0:
                if start_sum:
                    start_sum = False
                else:
                    start_sum = True
            if start_sum:
                sum_ += tmp.val
                tmp = tmp.next
            else:
                sum_node = ListNode(sum_)
                prev_sum_node.next = sum_node
                prev_sum_node = sum_node
                start_sum = False
                sum_ = 0
        return head.next


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


if __name__ == "__main__":
    sol = Solution()
    linked_list = convert_into_linked_list([0,3,1,0,4,5,2,0])
    res = sol.mergeNodes(linked_list)
    print(res)
