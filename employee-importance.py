"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(dict)

        for employee in employees:
            graph[employee.id] = {'imp': employee.importance, 'sub': employee.subordinates}

        def dfs(curr):
            if not graph[curr]['sub']:
                return graph[curr]['imp']

            ans = 0

            for sub in graph[curr]['sub']:
                ans += dfs(sub)

            return ans + graph[curr]['imp']
        
        return dfs(id)