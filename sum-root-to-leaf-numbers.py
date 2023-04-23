# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        nums = []

        def dfs(node):
            nonlocal ans, nums

            if not node:
                return

            nums.append(str(node.val))

            if not node.left and not node.right:
                print(nums)
                ans += int(''.join(nums))
                return
   
            
            if not dfs(node.left):
                nums.pop()
            
            if not dfs(node.right):
                nums.pop()

            

        dfs(root)

        return ans