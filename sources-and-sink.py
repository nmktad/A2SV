graph = []

sources, sink = [], []

for i in range(int(input())):
    mlist = list(map(int, input().split()))

    if mlist.count(1) == 0:
        sink.append(i+1)

    graph.append(mlist)

for col in range(len(graph[0])):
    sum = 0
    for row in range(len(graph)):
        sum += graph[row][col]

    if sum == 0:
        sources.append(col + 1)

print(len(sources), *sources)
print(len(sink), *sink)