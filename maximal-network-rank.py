class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for fr, to in roads:
            graph[fr].add(to)
            graph[to].add(fr)

        maxRank = 0

        for i in range(n):
            for j in range(i+1, n):
                temp = list(graph[i]) + list(graph[j])
                maxRank = max(maxRank, len(temp) - (1 if i in graph[j] else 0))

        return maxRank