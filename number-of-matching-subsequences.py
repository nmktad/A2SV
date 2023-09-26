class TrieNode:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.IsWordEnd = 0


class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def insert(self, word: str) -> None:
        last = self.root
        for char in word:
            if char not in last.children:
                last.children[char] = TrieNode(char)
            
            last = last.children[char]
        
        last.IsWordEnd += 1


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()

        for word in words: 
            trie.insert(word)
        
        occurence = defaultdict(list)
        occurence['*'] = [-1]

        for i, ch in enumerate(s):
            occurence[ch].append(i)
        
        def dfs(node, idx):
            count = 0
            pos = bisect_left(occurence[node.key], idx)
            if node.key == '*' or pos < len(occurence[node.key]):
                count += node.IsWordEnd
                for child in node.children:
                    count += dfs(node.children[child], occurence[node.key][pos]+1)
            
            return count

        return dfs(trie.root, -1)