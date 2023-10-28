class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        ind = {}

        for i, val in enumerate(nums):
            if tar - val in ind:
                return [i, ind[tar-val]]

            ind[val] = i

