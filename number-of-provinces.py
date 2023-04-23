class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i, connection in enumerate(isConnected):
            graph[i+1] = [j + 1 for j, x in enumerate(connection) if j != i and x == 1 ]
        
        count = 0

        visited = set()

        for node in graph.keys():
            if node not in visited:
                stack = [node]

                while stack:
                    curr = stack.pop()

                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)

                count += 1
        return count