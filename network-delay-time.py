class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstras(graph, start):
            heap = [(0, start)]
            distances = defaultdict(lambda : inf)
            distances[start] = 0
            visited = set()

            while heap:
                dist, node = heapq.heappop(heap)

                if node in visited:
                    continue

                visited.add(node)

                for child, weight in graph[node]:
                    if dist + weight < distances[child]:
                        distances[child] = dist + weight
                        heapq.heappush(heap, (dist + weight, child))

            if len(visited) != n:
                return -1
            return max(distances.values())
        
        graph = defaultdict(list)

        for st, dest, we in times:
            graph[st].append((dest, we))

        return dijkstras(graph, k)