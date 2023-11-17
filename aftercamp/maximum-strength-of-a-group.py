class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        def solve(i, curr, count):
            if i == len(nums): 
                if count: return curr
                return -inf
                
            return max(solve(i+1, curr * nums[i], count+1), solve(i+1, curr, count))

        return solve(0, 1, 0)
            