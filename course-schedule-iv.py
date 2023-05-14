class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        indegree = [0] * numCourses
        ancestors = [set() for _ in range(numCourses)]

        for fr, to in prerequisites:
            graph[fr].add(to)
            indegree[to] += 1

        queue = deque()

        for i in range(numCourses):
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
        
        return [fr in ancestors[to] for fr, to in queries]