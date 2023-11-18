class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n, m = len(wall), sum(wall[0])
        bricks = defaultdict(int)

        for row in wall:
            for acc in accumulate(row):
                bricks[acc] += 1

        ans = 0

        for i, val in bricks.items():
            if 0 < i < m:
                ans = max(ans, val)

        return n - ans