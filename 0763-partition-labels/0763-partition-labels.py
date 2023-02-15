class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idxes = {}
        ans = []
        
        for idx,val in enumerate(s):
            idxes[val] = idx
        
        curr = end = _sum = 0
        
        while end < len(s):
            # print(end, s[curr], idxes[s[curr]], ans)
            end = max(end,idxes[s[curr]])
            
            start = curr
            
            while curr < end:
                end = max(end,idxes[s[curr]])
                curr += 1
                
            if curr == end:
                ans.append(end-start+1)
                
                _sum += ans[-1]
                if _sum == len(s):
                    return ans
                
                curr += 1
        