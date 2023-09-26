class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]  

        curr.isEndOfWord = True
        
    def search(self, word: str) -> bool:
        queue = deque([self.root])

        for char in word:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if char == ".":
                    queue.extend(curr.children.values())

                elif char in curr.children:
                    queue.append(curr.children[char])

            if not queue: return False

        return any([queue.popleft().isEndOfWord for _ in range(len(queue))])