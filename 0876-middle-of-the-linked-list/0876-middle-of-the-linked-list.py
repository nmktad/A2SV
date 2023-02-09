# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lptr = rptr = head
        
        while rptr and rptr.next:
            lptr = lptr.next
            rptr = rptr.next.next
            
        return lptr