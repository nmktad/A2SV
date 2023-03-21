class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def freq(s):
            return s.count(min(s))
        
        ans = []

        for i in range(len(words)):
            words[i] = freq(words[i])

        words.sort()

        for query in queries:

            l, r = 0, len(words)-1
            target = freq(query)

            while l <= r:
                m = l + (r - l) // 2

                if words[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            
            ans.append(len(words)-l)
        return ans