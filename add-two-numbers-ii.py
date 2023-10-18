# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        head = ListNode()
        curr = head

        while l1 or l2:
            if l1 and l2:
                # print("adding", l1.val + l2.val, "to", curr.val)
                curr.val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                curr.val += l1.val
                l1 = l1.next
            elif l2:
                curr.val += l2.val
                l2 = l2.next
            if curr.val > 9:
                temp = curr.val
                curr.val = temp % 10
                curr.next = ListNode((temp // 10) % 10)
            else:
                curr.next = ListNode()
            curr = curr.next

        head = self.reverse(head)

        while head:
            if head.next and head.val == 0:
                head = head.next
            else:
                break

        return head

    
    def reverse(self, node):
        if not node.next:
            return node
        
        l, curr, r = None, node, node.next

        while r:
            curr.next = l
            l = curr
            curr = r
            r = r.next

        curr.next = l
        return curr