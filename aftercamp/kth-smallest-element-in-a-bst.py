class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k
            if not node: return

            left = inorder(node.left)
            
            if left != None: return left

            k -= 1

            if not k: return node.val
            
            return inorder(node.right)
        return inorder(root)