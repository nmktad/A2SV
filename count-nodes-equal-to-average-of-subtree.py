# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def helper(node):
            nonlocal count

            if not node:
                return 0, 0

            left, countL = helper(node.left)
            right, countR = helper(node.right)

            if node.val == (node.val + left + right) // (countL + countR + 1):
                count += 1

            return left + right + node.val, countL + countR + 1

        helper(root)

        return count