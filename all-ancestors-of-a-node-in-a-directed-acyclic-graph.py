class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        indegree = [0] * n
        ancestors = [set() for _ in range(n)]

        for fr, to in edges:
            graph[fr].add(to)
            indegree[to] += 1

        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            
            curr = queue.popleft()

            for nbr in graph[curr]:
                ancestors[nbr].add(curr)

                ancestors[nbr] = ancestors[nbr].union(ancestors[curr])
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    queue.append(nbr)

        for i in range(len(ancestors)):
            ancestors[i] = sorted(list(ancestors[i]))

        return ancestors