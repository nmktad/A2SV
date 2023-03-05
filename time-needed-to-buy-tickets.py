class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for i, ticket in enumerate(tickets):
            queue.append((i, ticket))

        ans = 0

        while True:
            i, ticket = queue.popleft()
            ans += 1

            ticket -= 1

            if i == k and ticket == 0:
                return ans
            if ticket > 0:
                queue.append((i, ticket))