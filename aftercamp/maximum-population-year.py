class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        years = []
        maxpopulation = 0
        ans = None
        
        for birth, death in logs:
            while years and birth >= years[0]:
                heapq.heappop(years)

            heapq.heappush(years, death)

            if maxpopulation < len(years):
                maxpopulation = len(years)
                ans = birth

        return ans

        