from collections import defaultdict

row, col = map(int,input().split())
ans=''
arr=[]

for i in range(row):
    arr.append(list(input()))

for i in range(row):
    for j in range(col):
        add=True
        tmpx=0
        tmpy=0
        
        while tmpx < row:
            if arr[tmpx][j] == arr[i][j] and tmpx != i:
                add=False
                break
            tmpx+=1
        while tmpy < col:
            if arr[i][tmpy] == arr[i][j] and tmpy != j:
                add=False
                break
            tmpy+=1
        if add:
            ans+=arr[i][j]
print(ans)