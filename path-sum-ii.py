# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], tar: int) -> List[List[int]]:
        def dfs(node, tar, ans, run):
            if not node:
                return 
            
            if not node.left and not node.right and node.val == tar:
                ans.append(run.copy() + [node.val])

            run.append(node.val)
            dfs(node.left, tar - node.val, ans, run)
            dfs(node.right, tar - node.val, ans, run)
            run.pop()

            return ans
        return dfs(root, tar, [], [])