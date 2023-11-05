class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        loss = defaultdict(int)
        for winner, loser in matches:
            loss[loser] += 1

            if winner not in loss:
                loss[winner] = 0

        for player, losses in loss.items():
            if losses == 0:
                ans[0].append(player)
            
            elif losses == 1:
                ans[1].append(player)

        ans[0].sort()
        ans[1].sort()

        return ans

            
        
        