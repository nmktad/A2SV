class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        roomCount = defaultdict(int)
        sofar = []
        roomAvail = [i for i in range(n)]

        meetings.sort()

        for st, end in meetings:
            while sofar and st >= sofar[0][0]:
                _, rid = heapq.heappop(sofar)
                heapq.heappush(roomAvail, rid)
            
            delay = 0

            if roomAvail:
                rid = heapq.heappop(roomAvail)

            else:
                delay = sofar[0][0] - st
                _, rid = heapq.heappop(sofar)

            heapq.heappush(sofar, [end + delay, rid])
            roomCount[rid] += 1

        ans = inf
        count = -1

        for room, nomeet in roomCount.items():
            if nomeet >= count:
                if nomeet == count:
                    ans = min(ans, room)
                else:
                    ans = room
                    count = nomeet


        return ans       