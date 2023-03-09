# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        _dict = defaultdict(list)

        def helper(level, node):
            if not node:
                return
            
            _dict[level].append(node.val)
            helper(level+1, node.left)
            helper(level+1, node.right)        

        helper(0, root)
        
        return _dict.values()