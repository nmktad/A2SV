class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        lptr, rptr = 0, 0
        count = 0
        
        for rptr in range(len(fruits)):
            window[fruits[rptr]] += 1
            
            while len(window) > 2:
                window[fruits[lptr]] -= 1
                
                if window[fruits[lptr]] == 0:
                    window.pop(fruits[lptr])
                lptr += 1
                
            count = max(count, rptr - lptr + 1)

        return count