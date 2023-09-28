class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = Counter(s)

        for char in s:
            if char not in stack:
                while stack and count[stack[-1]] > 0 and char < stack[-1]:
                    stack.pop()

                stack.append(char)
            count[char] -= 1

        return ''.join(stack)