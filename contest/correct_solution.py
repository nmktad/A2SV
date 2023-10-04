import heapq

arr = list(map(int, list(input())))
guess = input()
ans = []

heapq.heapify(arr)

n = len(arr)

for _ in range(n):
    curr = heapq.heappop(arr)
    
    if ans and ans[0] == 0:
        if curr != 0:
            ans.insert(0, curr)
        else:
            ans.append(curr)
    else:
        ans.append(curr)

ans = ''.join(map(str, ans))

if ans == guess:
    print("OK")
else:
    print("WRONG_ANSWER")

    