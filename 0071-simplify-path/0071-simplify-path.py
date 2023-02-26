class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        ans = "/"
        
        sections = path.split("/")
        
        for segment in sections:
            if segment == "" or segment == ".":
                continue
            elif segment == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(segment)
                
        return ans + '/'.join(stack)