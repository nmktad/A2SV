# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        
        while l1 and l2:
            num1.append(str(l1.val))
            num2.append(str(l2.val))
            l1 = l1.next
            l2 = l2.next
            
        if l1:
            while l1:
                num1.append(str(l1.val))
                l1 = l1.next
        
        if l2:
            while l2:
                num2.append(str(l2.val))
                l2 = l2.next
        
        num1 = reversed(num1)
        num2 = reversed(num2)
        
        num1 = int("".join(num1)) + int("".join(num2))
        
        num1 = reversed(str(num1))
        
        head = ListNode(-1)
        temp = head
        
        for i, char in enumerate(num1):
            temp.next = ListNode(int(char))
            temp = temp.next
                
        return head.next