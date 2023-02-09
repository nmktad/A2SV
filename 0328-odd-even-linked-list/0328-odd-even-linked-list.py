# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        oddHead = oddPtr = head
        evenHead = evenPtr = head.next
        
        while oddPtr.next and evenPtr.next:
            oddPtr.next = evenPtr.next
            oddPtr = oddPtr.next
            evenPtr.next = oddPtr.next
            evenPtr = evenPtr.next
        
        oddPtr.next = evenHead
    
        return head