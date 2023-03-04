class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        
        checking = defaultdict(int)
        
        presum = 0
        
        checking[0] = 1
        
        for val in nums:
            presum += val
            
            count += checking[presum % k]
            
            checking[presum % k] += 1
            
        return count