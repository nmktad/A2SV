# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(int)

        def traverse(root):
            if not root:
                return 

            traverse(root.left)
            ans[root.val] += 1
            traverse(root.right)
        
        
        traverse(root)

        mstack = []

        print()

        for key in ans:
            while mstack and ans[mstack[-1]] < ans[key]:
                mstack.pop()

            if not mstack or ans[mstack[-1]] == ans[key]:
                mstack.append(key)

        return mstack