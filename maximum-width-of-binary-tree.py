# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dictionary = defaultdict(list)

        def register(root, idx, lvl):
            if not root:
                return

            dictionary[lvl].append(idx)

            register(root.left, 2 * idx, lvl + 1)
            register(root.right, (2 * idx) + 1, lvl + 1)

        register(root, 1, 0)

        maxVal = float('-inf')

        for val in dictionary.values():
            maxVal = max(maxVal, (max(val) - min(val)) + 1)

        return maxVal