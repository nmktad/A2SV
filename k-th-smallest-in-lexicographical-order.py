class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        root = TrieNode(0)
        root.children = [TrieNode(n) for n in range(1, 10)]

        def belowCount(num):
            if num == 0: return n+1
            
            mul = 1
            ans = 0
            while num*mul <= n:
                ans += min(((num+1)*mul)-1, n) - num*mul + 1
                mul *= 10
        
            return ans

        def dfs(node):           
            nonlocal i
            if node.val != 0:
                node.children = [TrieNode(node.val * 10 + i) for i in range(10)]
                
            if i == k:
                return node.val
            if i + belowCount(node.val) <= k:
                i += belowCount(node.val)
                return
            else:
                i += 1
                for child in node.children:
                    ans =  dfs(child)
                    if ans:
                        return ans

        i = 0
        return dfs(root)