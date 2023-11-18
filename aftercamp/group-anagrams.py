class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for val in strs:
            dic[str(sorted(val))].append(val)

        return dic.values()
        
        