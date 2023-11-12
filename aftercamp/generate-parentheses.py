class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s, res):
            if len(s) == n * 2:
                res.append(''.join(s))
                return 

            if left < n:
                dfs(left + 1, right, s + ['('], res)

            if right < left:
                dfs(left, right + 1, s + [')'], res)

        res = []
        dfs(0, 0, [], res)
        return res
                
        