class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numstr = list(map(str, nums))
        
        numstr.sort()
        
        curr = [numstr[0]]
        
        for i in range(1, len(nums)):
            print(curr, numstr, numstr[i])

            if curr[-1] +numstr[i] > numstr[i]+curr[-1]:
                numstr[i-len(curr)] = numstr[i]
                numstr[i] = curr[-1]
            elif curr[-1] +numstr[i] == numstr[i]+curr[-1]:
                curr.append(numstr[i])
            else:
                curr = [numstr[i]]
                
        result = ''.join(reversed(numstr)) 
        if int(result)>0:
            return result
        else:
            return '0'
