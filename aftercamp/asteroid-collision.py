class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for val in asteroids:
            if val < 0:
                flag = True
                while ans and ans[-1] > 0 and abs(val) >= ans[-1]:
                    if ans[-1] == abs(val):
                        flag = False
                        ans.pop()
                        break

                    ans.pop()

                if not ans or ans[-1] < 0:
                    if not flag: continue
                    ans.append(val)

            else:
                ans.append(val)

        return ans
        