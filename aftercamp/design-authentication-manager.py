class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}
        self.timeline = deque()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl
        self.timeline.append((currentTime + self.ttl, tokenId))
    
    def _prune(self, currentTime):
        while self.timeline and self.timeline[0][0] <= (currentTime):
            _, token = self.timeline.popleft()

            if token in self.tokens and self.tokens[token] <= currentTime:
                del self.tokens[token]

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._prune(currentTime)

        if tokenId not in self.tokens:
            return 

        self.generate(tokenId, currentTime)       
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._prune(currentTime)
        return len(self.tokens)