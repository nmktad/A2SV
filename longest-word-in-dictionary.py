class TrieNode:
    def __init__(self, key):
        self.children = {}
        self.key = key
        self.isWordEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")
        self.root.isWordEnd = True

    def add(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            
            curr = curr.children[char]
        
        curr.isWordEnd = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        dic = Trie()

        for word in words:
            dic.add(word)
        
        def dfs(node):
            if not node.isWordEnd: return ""
            if len(node.children) == 0: return node.key

            lex = ""

            for child in node.children.values():
                res = dfs(child)

                if res == "": continue

                if lex == "":
                    lex = res

                elif len(res) > len(lex):
                    lex = res

                elif len(res) == len(lex):
                    if res < lex: lex = res

            if node.key == "*":
                return lex
            return node.key + lex

        return dfs(dic.root)