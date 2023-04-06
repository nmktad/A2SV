class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # build list

        graph = defaultdict(list)
        deleted = set()

        for vfrom, vto in edges:
            graph[vfrom].append(vto)
            deleted.add(vto)
        
        ans = []

        for i in range(n):
            if i not in deleted:
                ans.append(i)

        return ans