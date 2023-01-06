from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        _dict = defaultdict(list)
        answer = []
        
        for path in paths:
            [path, *files] = path.split()
            
            for file in files:
                [filename, content] = file.split("(")
                
                _dict[content].append(f"{path}/{filename}")
        
        for searches in _dict.values():
            if len(searches) > 1:
                answer.append(searches)
        return answer
            
            
            
            
    
# ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

#     [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]


# ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
    
    
#     [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]