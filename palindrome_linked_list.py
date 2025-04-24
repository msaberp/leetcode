from copy import copy
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        queue = []
        tmp = copy(head)
        while tmp is not None:
            queue.append(tmp.val)
            tmp = tmp.next
        
        _length = len(queue)
        while len(queue) > _length // 2:
            num = queue.pop()
            if head.val == num:
                head = head.next
                continue
            else:
                return False
            
        return True


if __name__ == "__main__":
    _input = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=1, next=None))))
    solution = Solution()
    output = solution.isPalindrome(_input)
    print(output)    

