# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        
        if not root1 and root2 or not root2 and root1:
            return False
        
        child = defaultdict(set)

        queue = deque([root1])

        while queue:
            curr = queue.popleft()
            
            if curr.left:
                child[curr.val].add(curr.left.val)
                queue.append(curr.left)

            if curr.right:
                child[curr.val].add(curr.right.val)
                queue.append(curr.right)

        queue.append(root2)

        while queue:
            curr = queue.popleft()
            temp = set()

            if curr.left:
                temp.add(curr.left.val)
                queue.append(curr.left)

            if curr.right:
                temp.add(curr.right.val)
                queue.append(curr.right)

            if temp != child[curr.val]:
                return False

        return True