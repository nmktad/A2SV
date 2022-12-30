# Enter your code here. Read input from STDIN. Print output to STDOUT

setA = set(input().split())
amount = int(input())

ans = True

for _ in range(amount):
    setB = set(input().split())
    areSetsEqual = len(setA) == len(setB)
    
    for val in setB:
        if val not in setA or areSetsEqual:
            ans = False
            break
        
    
print(ans)
