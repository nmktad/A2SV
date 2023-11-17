class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [key for key, value in Counter(nums).items() if value > len(nums) / 3]
        