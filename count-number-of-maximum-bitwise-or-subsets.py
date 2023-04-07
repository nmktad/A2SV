class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def returnBITOR(arr):
            temp = 0

            for num in arr:
                temp |= num

            return temp

        maxBOR = returnBITOR(nums)
        count = 0

        for i in range(2 ** len(nums)):
            num = bin(i)[2:]
            temp = []

            for i in range(len(num)-1, -1, -1):
                if num[i] == '1':
                    temp.append(nums[len(num) - 1 - i])
            
            # print(temp, returnBITOR(temp))
            if temp and maxBOR == returnBITOR(temp):
                count += 1

        return count