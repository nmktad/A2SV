from collections import deque
 
m, n, p = map(int, input().split())
 
grid = []
 
row, col = 0, 0
 
for i in range(m):
    temp = []
    for j, char in enumerate(input()):
        if char == "M":
            row = i
            col = j
        
        temp.append(char)
        
    grid.append(temp)
    
actions = list(map(int, input().split()))
 
for action in actions:
    if action == 0:
        continue
    else:
        if action == 1:
            row -= 1
        elif action == 2:
            row += 1
        elif action == 3:
            col -= 1
        elif action == 4:
            col += 1
 
directions = [(-1, 0), (1,0), (0, -1), (0,1)]
 
def isValid(r, c):
    return 0 <= r < m and 0 <= c < n
 
visited = set([(row, col)])
 
count = 0
 
queue = deque([(row, col)])
 
level = 0
count = 0
 
while queue and level <= p:
    itr = len(queue)
    
    # print(itr)
    
    count += itr
    
    for _ in range(itr):
        crow, ccol = queue.popleft()
        
        for r, c in directions:
            nrow, ncol = crow + r, ccol + c
            
            if isValid(nrow, ncol) and (nrow, ncol) not in visited and  grid[nrow][ncol] != "#":
                queue.append((nrow, ncol))
                visited.add((nrow, ncol))
    
    level += 1
 
print(count)