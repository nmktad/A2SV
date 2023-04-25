# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def backtrack(node, nums):
            nonlocal ans

            if not node:
                return
            
            nums.append(str(node.val))

            if not node.left and not node.right:
                ans += int(''.join(nums))
        
            backtrack(node.left, nums)
            backtrack(node.right, nums)

            nums.pop()

        backtrack(root, [])

        return ans