# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValidity(root, maximum):
            if not root:
                return True, maximum

            flag, maximum = checkValidity(root.left, maximum)

            if not flag or root.val <= maximum:
                return False, maximum

            maximum = root.val

            flag, maximum = checkValidity(root.right, maximum)

            return flag, maximum

        return checkValidity(root, float('-inf'))[0]