class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        

        probs = [0]*n
        probs[start_node] = 1
        heap = [(-1, start_node)]
        visited = set()

        while heap:
            prob, node = heappop(heap)
            prob *= -1

            if node in visited:
                continue
            
            visited.add(node)

            if node == end_node:
                return prob
            
            for neighbor, p in graph[node]:
                if prob*p > probs[neighbor]:
                    heappush(heap, (-prob*p, neighbor))
        
        return 0