# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0

        def traverse(node, parent, grandparent):
            nonlocal ans

            if not node:
                return

            if grandparent:
                if grandparent.val % 2 == 0:
                    ans += node.val

            traverse(node.left, node, parent)
            traverse(node.right, node, parent)

        traverse(root, None, None)
        return ans