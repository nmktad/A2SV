from collections import defaultdict, deque

def parallelCourses(n, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * (n + 1)

    for fr, to in prerequisites:
        graph[fr].append(to)
        indegree[to] += 1

    queue = deque()
    seen = set()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            seen.add(i)

    semester = 0     

    while queue:
        l = len(queue)

        for _ in range(l):
            curr = queue.popleft()

            for nbr in graph[curr]:
                if nbr not in seen:
                    indegree[nbr] -= 1

                    if indegree[nbr] == 0:
                        queue.append(nbr)
                        seen.add(nbr)

        semester += 1

    if len(seen) == n:
        return semester

    return -1
