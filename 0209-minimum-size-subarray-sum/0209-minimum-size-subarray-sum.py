class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _sum = nums[0]
        
        lptr = 0
        rptr = 0
        
        minlen = float('inf')
        
        while rptr < len(nums) and lptr < len(nums) and lptr <= rptr:
            
            # print(f"taking lptr on {nums[lptr]} and rptr on {nums[rptr]} the sum is {_sum} with minlen {minlen}")
            
            if nums[lptr] == target or nums[rptr] == target:
                return 1
            
            if _sum < target:
                if rptr < len(nums) - 1:
                    rptr += 1
                    _sum += nums[rptr]
                else:
                    break
            else:
                minlen = min(minlen, (rptr - lptr) + 1)
                if lptr < len(nums) - 1:
                    _sum -= nums[lptr]
                    lptr += 1

                else:
                    break
        
        return minlen if minlen != float('inf') else 0