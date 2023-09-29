# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0 : return

        root = TreeNode(preorder[0])

        if len(preorder) == 1: return root

        mid = 1

        while mid < len(preorder) and preorder[mid] < preorder[0]:
            mid += 1

        root.left = self.bstFromPreorder(preorder[1:mid])
        root.right = self.bstFromPreorder(preorder[mid:]) if mid < len(preorder) else None
        
        return root