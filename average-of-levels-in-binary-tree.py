# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []

        while queue:
            total = 0

            itr = len(queue)

            for _ in range(itr):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            ans.append(total/itr)
            
        return ans