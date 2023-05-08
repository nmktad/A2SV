class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-val for val in piles]
        heapq.heapify(piles)

        for _ in range(k):
            heapq.heappush(piles, (heapq.heappop(piles) // 2))

        return abs(sum(piles))