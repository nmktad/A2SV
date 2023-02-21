n = int(input())
 
for _ in range(n):
    string = input()
    ans = []
    prev = ""
    
    for ptr, char in enumerate(string):
        if prev != "":
            prev = ""
            continue
        if ptr < len(string) - 1 and string[ptr] == string[ptr + 1]:
            prev = char
            continue 
        else:
            if prev != string[ptr] and string[ptr] not in ans:
                ans.append(string[ptr])
    ans.sort()
    print("".join(ans))
