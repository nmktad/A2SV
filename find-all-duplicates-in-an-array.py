class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        lptr = 0

        ans = []

        while lptr < len(nums):
            if nums[lptr] == 0 or (nums[lptr] - 1 == lptr):
                lptr += 1
            else:
                if nums[nums[lptr]-1] != nums[lptr]:
                    nums[nums[lptr]-1], nums[lptr] = nums[lptr], nums[nums[lptr]-1]
                else:
                    ans.append(nums[lptr])
                    nums[lptr] = 0

        return ans