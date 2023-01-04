from collections import Counter
 
[nstu, nques] = map(int, input().split())
 
_dict = {}
 
for i in range(1, nques + 1):
    _dict[i] = []
 
for i in range(nstu):
    answers = input()
    
    for i, char in enumerate(answers):
        _dict.get(i+1).append(char)
 
ans = []
 
for key in _dict:
    ans.append(Counter(_dict[key]).most_common(1)[0][1])
sum = 0
 
points = list(map(int, input().split()))
 
for i in range(nques):
    sum += points[i] * ans[i]
    
print(sum)
