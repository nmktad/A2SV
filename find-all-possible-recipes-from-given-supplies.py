class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for i in range(len(recipes)):
            for item in ingredients[i]:
                graph[item].add(recipes[i])
                indegree[recipes[i]] += 1

        recipes = set(recipes)

        queue = deque(supplies)

        ans = []

        while queue:
            curr = queue.popleft()

            if curr in recipes:
                ans.append(curr)

            for nbr in graph[curr]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    queue.append(nbr)

        return ans