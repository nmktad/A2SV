class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        ans = []

        for fr,to in adjacentPairs:
            graph[fr].append(to)
            graph[to].append(fr)
            indegree[fr] += 1
            indegree[to] += 1

        seen = set()
        queue = deque()

        for i in graph:
            if indegree[i] == 1:
                queue.append(i)
                seen.add(i)
                break

        while queue:
            curr = queue.popleft()

            ans.append(curr)
            seen.add(curr)

            for nbr in graph[curr]:
                if nbr not in seen:
                    queue.append(nbr)
                    seen.add(nbr)
        return ans