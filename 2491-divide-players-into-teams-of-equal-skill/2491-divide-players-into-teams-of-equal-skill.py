class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        
        skill.sort()
        
        rptr = len(skill) - 1
        lptr = 0
        
        myList = []
        
        check = skill[rptr] + skill[lptr]
        
        while rptr > lptr:
            if skill[rptr] + skill[lptr] != check:
                return -1
            myList.append((skill[rptr], skill[lptr]))
            rptr -= 1
            lptr += 1
        
        ans = 0
        
        for val in myList:
            ans += reduce((lambda x, y: x * y), val)
            
        return ans
        