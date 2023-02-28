class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lptr = 0
        counter = defaultdict(int)
        ans = 0
        
        for rptr, char in enumerate(s):
            counter[char] += 1
            
            # print(f"counter dict is {counter} and subarray of {s[lptr:rptr]}")
            
            while (rptr - lptr + 1) - max(counter.values()) > k:
                counter[s[lptr]] -= 1
                lptr += 1
                
            ans = max(ans, rptr - lptr + 1)
            
        return ans
            