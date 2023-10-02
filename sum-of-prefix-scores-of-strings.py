class TrieNode:
    def __init__(self, key):
        self.children = {}
        self.score = 0

class Trie:
    def __init__(self):
        self.root = TrieNode("*")
    
    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)

            curr = curr.children[char]
            curr.score += 1

    def getScore(self, word):
        curr = self.root

        accum = 0

        for char in word:
            curr = curr.children[char]
            accum += curr.score

        return accum

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        return [trie.getScore(word) for word in words]