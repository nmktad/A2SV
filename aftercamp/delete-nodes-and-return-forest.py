# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], td: List[int]) -> List[TreeNode]:
        td = set(td)
        ans = {}

        def helper(node, parent):
            nonlocal ans, td
            if not node: return

            if node.val in td:
                if node in ans:
                    del ans[node]
                
                if node.left:
                    ans[node.left] = True
                
                if node.right:
                    ans[node.right] = True
                
                if parent:
                    if parent.left and parent.left.val == node.val:
                        parent.left = None
                
                    if parent.right and parent.right.val == node.val:
                        parent.right = None
            
            helper(node.left, node)
            helper(node.right, node)

        helper(root, None)
        if root.val not in td:
            ans[root] = True

        return ans.keys()

        