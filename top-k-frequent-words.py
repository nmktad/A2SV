class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heaped = [(-counts[key], key) for key in counts]

        heapq.heapify(heaped)
            
        return [heapq.heappop(heaped)[1] for _ in range(k)]