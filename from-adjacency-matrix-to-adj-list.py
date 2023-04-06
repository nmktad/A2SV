from collections import defaultdict

graph = defaultdict(list)

for i in range(int(input())):
    oper = input().split()

    for j in range(len(oper)):
        if oper[j] == '1':
            graph[i+1].append(j+1)

for key in graph:
    print(len(graph[key]), *sorted(graph[key]))