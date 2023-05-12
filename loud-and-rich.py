class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * len(quiet)
        quiet_dict = {}

        for i, val in enumerate(quiet):
            quiet_dict[val] = i

        for rp, pp in richer:
            graph[rp].append(pp)
            indegree[pp] += 1

        ans = quiet
        queue = deque()

        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)

        while queue:

            curr = queue.popleft()
            for nbr in graph[curr]:
                ans[nbr] = min(ans[nbr], ans[curr], quiet[nbr], quiet[curr])

                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        for i in range(len(ans)):
            ans[i] = quiet_dict[ans[i]]

        return ans