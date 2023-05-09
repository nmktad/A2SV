class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].add(course)
            indegree[course] += 1

        queue = deque()

        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)

        ans = []

        while queue:
            curr = queue.popleft()

            ans.append(curr)

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(ans) != numCourses:
            return []

        return ans