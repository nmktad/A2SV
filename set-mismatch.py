class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lptr = 0

        ans = []

        while lptr < len(nums):
            if nums[lptr] - 1 == lptr or nums[lptr] == 0:
                lptr += 1
                continue

            if nums[nums[lptr]-1] == nums[lptr]:
                ans.append(nums[lptr])
                nums[lptr] = 0
                continue

            nums[nums[lptr]-1], nums[lptr] = nums[lptr], nums[nums[lptr]-1]

        return ans+[nums.index(0) + 1]