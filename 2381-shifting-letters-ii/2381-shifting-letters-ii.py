class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        presum = [0] * (len(s) + 1)
        
        for val in shifts:
            left, right, direction = val
            
            if direction == 0:
                presum[left] -= 1
                presum[right+1] += 1
                
            else:
                presum[left] += 1
                presum[right+1] -= 1
                
        for i in range(1, len(presum)):
            presum[i] += presum[i-1]
            
        ans = []
        
        for i in range(len(presum)-1):
            ans.append(chr(((ord(s[i]) - 97 + presum[i]) % 26) + 97))
        
        return "".join(ans)