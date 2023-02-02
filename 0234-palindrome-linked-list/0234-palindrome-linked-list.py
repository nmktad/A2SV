# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        if head.next:
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next


            lptr = None
            mptr = slow
            rptr = slow.next

            while rptr:
                mptr.next = lptr
                lptr = mptr
                mptr = rptr
                rptr = rptr.next


            mptr.next = lptr

            while mptr and mptr.next != head:
                if head.val != mptr.val:
                    return False

                mptr = mptr.next
                head = head.next

        return True
            