from collections import defaultdict

num_ver = int(input())

graph = defaultdict(list)

for _ in range(int(input())):
    oper = list(map(int, input().split()))

    if oper[0] == 1:
        v1, v2 = oper[1:]

        graph[v1].append(v2)
        graph[v2].append(v1)       
    else:
        v = oper[1:][0]
        print(*graph[v])