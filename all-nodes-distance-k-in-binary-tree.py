# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}

        def bfs(root, dist):
            queue = deque([root])
            seen = set([root])

            while queue:
                l = len(queue)

                if dist == 0:
                    return [node.val for node in queue if node]

                for _ in range(l):
                    curr = queue.popleft()

                    if not curr:
                        continue

                    if curr.left and curr.left not in seen:
                        queue.append(curr.left)
                        seen.add(curr.left)
                    
                    if curr.right and curr.right not in seen:
                        queue.append(curr.right)
                        seen.add(curr.right)

                    if curr in parents and parents[curr] not in seen:
                        queue.append(parents[curr])
                        seen.add(parents[curr])

                dist -= 1

        def dfs(node, parent):
            if not node:
                return

            parents[node] = parent

            if node == target:
                return bfs(node, k)

            left = dfs(node.left, node)
            right = dfs(node.right, node)

            return left if left else right

        ans = dfs(root, None)

        if not ans:
            return []

        return ans