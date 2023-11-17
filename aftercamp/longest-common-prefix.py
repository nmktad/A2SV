class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            curr = strs[0][i]

            for word in strs:
                try:
                    if word[i] != curr:
                        return strs[0][:i]
                except IndexError:
                    return strs[0][:i]
                    
        return strs[0]
