class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lptr = 0

        while lptr < len(nums):
            if nums[lptr] == 0 or (nums[lptr] - 1 == lptr):
                lptr += 1
            else:
                if nums[nums[lptr]-1] != nums[lptr]:
                    nums[nums[lptr]-1], nums[lptr] = nums[lptr], nums[nums[lptr]-1]
                else:
                    nums[lptr] = 0

        return [i + 1  for i, val in enumerate(nums) if val == 0]