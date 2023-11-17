# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = TreeNode()
        curr = ans
        prev = None

        def inorder(node):
            nonlocal curr, prev

            if not node:
                return

            inorder(node.left)

            curr.val = node.val
            prev = curr
            curr.right = TreeNode()
            curr = curr.right

            inorder(node.right)

        inorder(root)
        prev.right = None
        return ans
        