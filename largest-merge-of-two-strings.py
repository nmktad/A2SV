class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l, r, merged = 0, 0, ""

        while l < len(word1) and r < len(word2):
            if word1[l:] > word2[r:]:
                merged += word1[l]
                l += 1
                continue

            merged += word2[r]
            r += 1
        
        merged += word1[l:] + word2[r:]
        return merged