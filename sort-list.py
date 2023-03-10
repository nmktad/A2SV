# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        
        left, right = self.splitMiddle(head)
        ans = self.sortList(left)
        ans2 = self.sortList(right)

        return self.mergeSort(ans, ans2)


    def splitMiddle(self, head):
        if not head.next:
            return None, None

        left = right = head

        while right and right.next:
            right = right.next.next
            left = left.next

        right = head

        while right:
            
            if right.next != left:
                right = right.next
            else:
                break

        right.next = None

        return head, left


    def mergeSort(self, head1, head2):
        newhead = ListNode()
        ret = newhead

        while head1 or head2:
            if head1 and head2:
                if head1.val <= head2.val:
                    newhead.next = ListNode(head1.val)
                    head1 = head1.next
                else:
                    newhead.next = ListNode(head2.val)
                    head2 = head2.next
            elif head1:
                newhead.next = ListNode(head1.val)
                head1 = head1.next
            elif head2:
                newhead.next = ListNode(head2.val)
                head2 = head2.next

            newhead = newhead.next

        return ret.next