class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        ans = ""
        for i, char in enumerate(command):
            if char == "G":
                ans += "G"
            elif char == ")":
                if stack.pop() == "(":
                    ans += "o"
                else: 
                    ans += "al"
                    stack.pop()
                    stack.pop()
            else: stack.append(char)
                
        return ans