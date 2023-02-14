# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(500, head)
        temp = dummy
        
        while dummy.next and dummy.next.next:
            nnode = dummy.next.next
            
            # print("comparing", dummy.next.val, nnode.val)
            if dummy.next.val == nnode.val:
                if nnode.next:
                    
                    while nnode and nnode.next and nnode.val == nnode.next.val:
                        # print("while", nnode.val, "equals", nnode.next.val)
                        nnode = nnode.next

                dummy.next = nnode.next
            else:
                dummy= dummy.next
            
        return temp.next