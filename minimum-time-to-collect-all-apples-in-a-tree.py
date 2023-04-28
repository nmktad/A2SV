class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for fr, to in edges:
            graph[fr].append(to)
            graph[to].append(fr)

        

        def dfs(node, parent):
            if not graph[node]:
                if not hasApple[node]:
                    return False, 0
                else:
                    return True, 1

            flag, count = hasApple[node], 0

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                cflag, currCount = dfs(neighbor, node)

                # print(cflag, currCount, neighbor)

                if cflag:
                    flag = True

                count += currCount
            
            # print(count, node, flag)
            return flag, count + 1 if flag else 0

        flag, res = dfs(0, None)

        if not flag:
            return 0

        return (res - 1) * 2