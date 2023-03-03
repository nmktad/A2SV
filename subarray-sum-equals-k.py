class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        dictionary = defaultdict(int)
        presum = 0
        
        dictionary[0] += 1
        
        for val in nums:
            presum += val
            
            counter += dictionary[presum - k]
            
            dictionary[presum] += 1
                    
        return counter