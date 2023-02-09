# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        
        ptr1 = list1
        ptr2 = list2
        ans = []
        
        while ptr1 or ptr2:
            if ptr1 and ptr2:
                if ptr1.val < ptr2.val:
                    ans.append(ptr1.val)
                    ptr1 = ptr1.next
                    continue
                else:
                    ans.append(ptr2.val)
                    ptr2 = ptr2.next
                    continue
            else:
                if ptr1:
                    ans.append(ptr1.val)
                    ptr1 = ptr1.next
                elif ptr2:
                    ans.append(ptr2.val)
                    ptr2 = ptr2.next
                    
        ptr1 = list1
        
        while ptr1.next:
            ptr1 = ptr1.next
            
        ptr1.next = list2
        
        ptr1 = list1
        ans.reverse()
        
        while ptr1:
            ptr1.val = ans.pop()
            ptr1 = ptr1.next
            
        return list1
            
            
        
            
        
        