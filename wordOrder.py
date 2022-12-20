num = int(input())
words = list(input() for i in range(num))

dict = {}

for word in words:
    if word in dict:
        dict[word] = dict.get(word) + 1
    else:
        dict[word] = 1
      
sec_ans = ""        
for val in list(dict.values()):
    sec_ans += f"{val} "
    
        
print(f"{len(dict)}\n{sec_ans}")