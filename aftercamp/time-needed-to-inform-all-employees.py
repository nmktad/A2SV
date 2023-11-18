class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for e,m in enumerate(manager):
            graph[m].append(e)

        queue = deque([(0, headID)])
        ans = 0

        while queue:
            for _ in range(len(queue)):
                time, curr = queue.popleft()

                ans = max(ans, time)

                for nbr in graph[curr]:
                    if manager[nbr] == curr:
                        queue.append((time+informTime[manager[nbr]], nbr))

        return ans