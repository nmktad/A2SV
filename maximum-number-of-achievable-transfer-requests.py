class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        maxTransfer = 0
        netChange = [0]*n

        def backtrack(start, accepted):
            nonlocal maxTransfer
            
            if all([i == 0 for i in netChange]):
                maxTransfer = max(maxTransfer, accepted)
            
            for i in range(start, len(requests)):
                netChange[requests[i][0]] -= 1
                netChange[requests[i][1]] += 1

                backtrack(i+1, accepted+1)

                netChange[requests[i][0]] += 1
                netChange[requests[i][1]] -= 1

        backtrack(0, 0)
        return maxTransfer