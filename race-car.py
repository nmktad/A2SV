class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1)])
        visited = set()
        visited.add((0,1))

        count = 0

        while queue:
            cl = len(queue)

            for _ in range(cl):
                pos, speed = queue.popleft()
                
                if pos == target:
                    return count

                if (pos + speed, speed * 2) not in visited:
                    queue.append((pos + speed, speed * 2))
                    visited.add((pos + speed, speed * 2))

                if speed > 0:
                    if (pos, -1) not in visited:
                        queue.append((pos, -1))
                        visited.add((pos, -1))
                else:
                    if (pos, 1) not in visited:
                        queue.append((pos, 1))
                        visited.add((pos, 1))

            count += 1

        return count