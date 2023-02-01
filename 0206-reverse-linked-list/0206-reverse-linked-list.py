# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lptr = None
        if head:
            rptr = head.next

            while rptr:
                head.next = lptr 
                lptr = head
                head = rptr
                rptr = rptr.next

            head.next = lptr

        return head
        