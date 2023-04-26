class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = defaultdict(set)

        target = len(graph) - 1

        for i, nodes in enumerate(graph):
            for node in nodes:
                g[i].add(node)

        ans = []

        def rec(node, curr):
            nonlocal ans
            if target == node:
                ans.append(curr + [node])
                return
            
            for neighbor in graph[node]:
                rec(neighbor, curr + [node])

        rec(0, [])

        return ans