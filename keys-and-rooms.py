class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()

        while queue:
            curr = queue.popleft()
            visited.add(curr)

            for key in rooms[curr]:
                if key not in visited:
                    queue.append(key)
        
        return len(visited) == len(rooms)