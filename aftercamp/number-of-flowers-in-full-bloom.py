class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        ans = []
        sort_start = [flower[0] for flower in flowers]
        sort_end = [flower[1] for flower in flowers]

        sort_start.sort()
        sort_end.sort()

        for i in people:
            ans.append(bisect_right(sort_start,i)-bisect_left(sort_end,i))
        return ans