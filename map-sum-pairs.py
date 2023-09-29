class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False
        self.value = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def dfs(self, node):
        if not len(node.children):
            return node.value

        ans = 0 if not node.isWordEnd else node.value

        for child in node.children.values():
            ans += self.dfs(child)

        return ans

    def insert(self, key: str, val: int) -> None:
        curr = self.root

        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.isWordEnd = True
        curr.value = val
        
    def sum(self, prefix: str) -> int:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return 0

            curr = curr.children[char]

        return self.dfs(curr)


        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)