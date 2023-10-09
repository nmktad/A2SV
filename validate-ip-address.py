class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIP4(s):
            try:
                return str(int(s))==s and 0<=int(s)<=255
            except:
                return False
            
        def isIP6(s):
            if len(s)>4:
                return False

            try:
                int(s,16)
                return True
            except:
                return False
                
        if "." in queryIP:
            arr = queryIP.split(".")
            if len(arr) == 4 and all(isIP4(n) for n in arr):
                return "IPv4"


        elif ":" in queryIP:
            arr = queryIP.split(":")
            if len(arr) == 8 and all(isIP6(n) for n in arr):
                return "IPv6"
        
        return "Neither"