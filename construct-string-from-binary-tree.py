# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []

        def recurse(node):
            nonlocal ans

            if not node:
                return
        
            ans.append(str(node.val))
        
            if node.left:
                ans.append('(')
                recurse(node.left)
                ans.append(')')
            
            if not node.left and node.right:
                ans.append('()')

            if node.right:
                ans.append('(')
                recurse(node.right)
                ans.append(')')

        recurse(root)
        return ''.join(ans)