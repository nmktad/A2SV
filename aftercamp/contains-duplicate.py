class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for val in nums:
            if val not in s:
                s.add(val)
            else:
                return True

        return False