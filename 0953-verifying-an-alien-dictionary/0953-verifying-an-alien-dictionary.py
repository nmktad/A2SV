class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {}
     
        for i in range(len(order)):
            ordering[order[i]] = i

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            
            for word_idx in range(len(word1)):
                if word_idx == len(word2):
                    return False
                if word1[word_idx] != word2[word_idx]:
                    if ordering[word2[word_idx]] < ordering[word1[word_idx]]:
                        return False
                    break
        return True