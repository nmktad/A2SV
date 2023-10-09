# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue, ans = deque([(1, root)]), 1

        while queue:
            ans = max(ans, (queue[-1][0] - queue[0][0]) + 1)
            for _ in range(len(queue)):
                idx, curr = queue.popleft()

                if curr.left:
                    queue.append((2*idx, curr.left))
                if curr.right:
                    queue.append((((2*idx)+1), curr.right))
        return ans