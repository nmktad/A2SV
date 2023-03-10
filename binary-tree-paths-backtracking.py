# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def helper(root, arr):
            if not root:
                return 

            if not root.left and not root.right:
                ans.append('->'.join(list(map(str, arr+[root.val]))))
                return
            arr.append(root.val)
            helper(root.left, arr)
            helper(root.right, arr)
            arr.pop()

        helper(root, [])

        return ans
