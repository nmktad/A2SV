class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True]*(right+1)
        is_prime[0] = is_prime[1] = False

        for i in range(ceil(sqrt(right))+1):
            if is_prime[i]:
                for j in range(2*i, right+1, i):
                    is_prime[j] = False

        ans = [-1, -1]
        # print([(i, val) for i, val in enumerate(is_prime)])

        last = 0

        while -1 in ans or left <= right:
            if left > right:
                break
            if is_prime[left]:
                # print('ans include', ans, 'the curr is', last, left)
                if ans[0] == -1:
                    ans[0] = left
                elif ans[1] == -1:
                    ans[1] = left
                else:
                    if ans[1] - ans[0] > left - last:
                        ans[0] = last
                        ans[1] = left

                last = left
            left += 1

        if -1 in ans:
            return [-1, -1]
            
        return ans