class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        presum = [1 if n % 2 == 1 else 0 for n in nums]

        for i in range(1, len(nums)):
            presum[i] += presum[i-1]

        ans = 0
        dic = defaultdict(int)

        dic[0] = 1

        for num in presum:
            ans += dic[num-k]                
            dic[num] += 1

        return ans