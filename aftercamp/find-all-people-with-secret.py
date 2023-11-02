class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        rep = {i:i for i in range(n)}
        meet = defaultdict(list)

        def find(x):
            if x != rep[x]:
                rep[x] = find(rep[x])

            return rep[x]

        
        def union(x, y):
            rx, ry = find(x), find(y)

            if rx != ry:
                if rx == 0:
                    rep[ry] = rx
                else:
                    rep[rx] = ry

        meetings = sorted(meetings, key=lambda x: x[2])

        for px, py, time in meetings:
            meet[time].append([px, py])

        # print(meet)
        union(0, firstPerson)

        for time, meetings in meet.items():
            for px, py in meetings:
                union(px, py)

            for px, py in meetings:
                if find(px) != 0:
                    rep[px] = px

                if find(py) != 0:
                    rep[py] = py

        ans = []
        # print("after merging", rep)

        for item, val in rep.items():
            if val != 0:
                continue
            ans.append(item)
        
        return ans