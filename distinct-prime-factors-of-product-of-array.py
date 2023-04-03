class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prod = 1
        primes = set()

        for val in nums:
            d = 2

            while d * d <= val:
                while val % d == 0:
                    primes.add(d)
                    val //= d
                
                if d != 2:    
                    d += 2
                else:
                    d += 1
        
            if val > 1:
                primes.add(val)

        return len(primes)