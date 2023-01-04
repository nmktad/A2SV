num = input()
 
ans = ""
 
for i, char in enumerate(num):
    if i == 0 and 9 - int(char) == 0:
        ans += char
        continue
        
    
    if 9 - int(char) < int(char):
        ans += str(9-int(char))
    else:
        ans += char
 
print(ans)
