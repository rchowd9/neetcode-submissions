# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        curr = head
        while curr is not None:
            len += 1
            curr = curr.next
        
        target = len - n + 1

        if target == 1:
            return head.next

        curr = head
        for _ in range(target - 2):
            curr = curr.next

        curr.next = curr.next.next

        return head