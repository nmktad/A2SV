class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValidShippingWeight(takes, days, arr):
            if max(arr) > takes:
                return False

            days_taken = 0
            temp = takes

            for weight in arr:
                if temp >= weight:
                    temp -= weight
                else:
                    days_taken += 1
                    temp = takes
                    temp -= weight

            return days_taken < days

        l = 1
        r = sum(weights)    
        a = float('inf')

        while l <= r:
            m = l + (r - l) // 2

            if isValidShippingWeight(m, days, weights):
                a = m
                r = m - 1
            else:
                l = m + 1

        
        return a