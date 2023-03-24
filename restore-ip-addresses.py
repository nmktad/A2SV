class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def helper(start, arr):
            if start == len(s):
                if len(arr) == 4:
                    ans.append('.'.join(arr))
                    return

            for i in range(start, len(s)):
                if int(s[start:i+1]) <= 255 and (len(s[start:i+1]) == 1 or s[start] != "0"):
                    helper(i+1, arr+[s[start:i+1]])
        
        helper(0, [])
        
        return ans