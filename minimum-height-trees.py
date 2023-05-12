class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        if n == 2:
            return [0, 1]
            
        edgeCount = [0] * n

        graph = defaultdict(list)

        for fr, to in edges:
            graph[fr].append(to)
            graph[to].append(fr)

            edgeCount[fr] += 1
            edgeCount[to] += 1

        queue = deque()
        seen = set()

        for i, count in enumerate(edgeCount):
            if count == 1:
                queue.append(i)
                seen.add(i)

        while n > 2:
            for _ in range(len(queue)):

                curr = queue.popleft()
                n -= 1

                for nbr in graph[curr]:
                    if nbr not in seen:
                        edgeCount[nbr] -= 1

                        if edgeCount[nbr] == 1:
                            queue.append(nbr)
                            seen.add(nbr)
        return list(queue)