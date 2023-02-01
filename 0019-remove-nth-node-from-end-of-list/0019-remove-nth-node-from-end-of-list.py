# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lptr = rptr = head
        
        if n == 1:
            if rptr.next:
                flag = True
                while rptr.next:
                    rptr = rptr.next
                    if flag == True:
                        flag = False
                    else:
                        lptr = lptr.next
                
            if head == rptr:
                head = head.next
            
            lptr.next = None
            return head
        
        for _ in range(n):
            rptr = rptr.next
        
        if rptr:
            while rptr.next:
                rptr = rptr.next
                lptr = lptr.next
                
        

            if lptr.next:
                lptr.next = lptr.next.next
                
        else:
            print(head)
            head = head.next
        
        return head
            
            