class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)

        if '0000' in visited:
            return -1

        queue = deque(['0000'])

        count = 0

        while queue:            
            cl = len(queue)

            for _ in range(cl):
                curr = queue.popleft()

                if curr == target:
                    return count

                for i in range(8):
                    
                    newkey = []

                    if i < 4:
                        for j, char in enumerate(curr):
                            if i % 4 == j:
                                newkey.append(str((int(char) + 1) % 10))
                            else:
                                newkey.append(char)
                    else:
                        for j, char in enumerate(curr):
                            if i % 4 == j:
                                newkey.append(str((int(char) - 1) % 10))
                            else:
                                newkey.append(char)

                    newkey = ''.join(newkey)

                    if newkey not in visited:
                        queue.append(newkey)
                        visited.add(newkey)

            count += 1

        return -1