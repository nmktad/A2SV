# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        count = 1
        ptr = head
        
        while ptr.next:
            ptr = ptr.next
            count += 1
        
        ptr.next = head
        steps = count - k % count
        
        for _ in range(steps-1):
            head = head.next
            
        temp = head
        head = head.next
        temp.next = None
        
        return head