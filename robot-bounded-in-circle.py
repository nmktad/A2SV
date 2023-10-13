class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, d = 0, 0, 0

        for i in range(4):
            for ch in instructions:
                if ch == "G":
                    if d == 0:
                        y += 1
                    elif d == 1:
                        x += 1
                    elif d == 2:
                        y -= 1
                    elif d == 3:
                        x -= 1
                
                if ch == "L":
                    d = (d - 1) % 4
                if ch == "R":
                    d = (d + 1) % 4

            if (x, y) == (0, 0):
                return True

        return False