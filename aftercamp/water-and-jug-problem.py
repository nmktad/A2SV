class Solution:
    def canMeasureWater(self, j1: int, j2: int, t: int) -> bool:
        lo, hi = 0, j1 + j2
        candidates = [j1, j2, -j1, -j2]

        que = deque([0])
        visited = set([0])

        while que:

            num = que.popleft()
            if num == t:
                return True

            for cand in candidates:
                if 0 <= num+cand <= j1+j2 and num+cand not in visited:
                    que.append(num+cand)
                    visited.add(num+cand)

        return False