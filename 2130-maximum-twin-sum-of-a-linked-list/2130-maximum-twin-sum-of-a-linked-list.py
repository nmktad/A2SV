# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lptr = rptr = head
    
        while rptr:
            lptr = lptr.next
            rptr = rptr.next.next
            
        mptr = lptr
        lptr = None
        rptr = mptr.next

        while rptr:
            mptr.next = lptr
            lptr = mptr
            mptr = rptr
            rptr = rptr.next
            
        mptr.next = lptr
            
        _max = 0
        
        while mptr and head:
            _max = max(_max, mptr.val + head.val)
            mptr = mptr.next
            head = head.next
            
        return _max
            
            