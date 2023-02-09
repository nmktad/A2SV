# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        lptr = rptr = head
        
        while rptr and rptr.next and lptr:
            rptr = rptr.next.next
            lptr = lptr.next
            
            if rptr == lptr:
                rptr = head
                
                while rptr != lptr:
                    rptr = rptr.next
                    lptr = lptr.next
                    
                return lptr
        
        return None