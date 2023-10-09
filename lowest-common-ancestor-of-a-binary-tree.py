# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if not root:
                return False, root

            if root.val == p.val or root.val == q.val:
                return True, root

            lflag, left = helper(root.left, p, q)
            rflag, right = helper(root.right, p, q)

            if lflag and rflag:
                return True, root
            elif lflag and not rflag or not lflag and rflag:
                return True, left if lflag else right
            else:
                return False, 0
        
        return helper(root, p, q)[1]