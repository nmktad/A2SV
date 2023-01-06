class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        _list = []
        ptr = 0
        
        for i, char in enumerate(s):
            if ptr < len(spaces) and i == spaces[ptr]:
                _list.append(f" {char}")
                ptr += 1
            else:
                _list.append(char)
            
        return ''.join(_list)
            