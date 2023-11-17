class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted([(self.getOrder(x), x) for x in range(lo, hi+1)])[k-1][1]
    
    def getOrder(self, x):
        count = 0

        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1

            count += 1
        
        return count
        

        