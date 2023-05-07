# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for root in lists:
            while root:
                heapq.heappush(heap, root.val)
                root = root.next
        
        cur = head = ListNode()

        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        
        return head.next