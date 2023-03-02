class Solution:
    def decodeString(self, s: str) -> str:
        def decoder(s, i):       
            result = []
            num = "0"

            while i < len(s):
                if s[i].isdigit():
                    num += s[i]
                elif s[i] == '[':
                    string, end = decoder(s, i + 1)
                    result.append(int(num) * string)
                    i = end
                    num = "0"
                elif s[i] == ']':
                    return ''.join(result), i
                else:
                    result += s[i]
                i += 1
            
            return ''.join(result), i
                
        return decoder(s, 0)[0]