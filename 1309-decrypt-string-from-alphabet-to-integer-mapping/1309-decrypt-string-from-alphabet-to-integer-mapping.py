class Solution:
    def freqAlphabets(self, s: str) -> str:
        l_ptr = 0
        r_ptr = 2
        answer = ''
                
        while l_ptr <= len(s) - 1:
            if r_ptr <= len(s) - 1 and s[r_ptr] == '#':
                answer += chr(int(s[l_ptr:r_ptr]) + 96)
                l_ptr += 3
                r_ptr += 3
            else:
                answer += chr(int(s[l_ptr]) + 96)
                l_ptr += 1
                r_ptr += 1
                
        return answer

            
        
            
                
                
            
                
                
            
        