class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x, y = 0, 0
        visited = set()
        ans = []
        isValid = lambda x, y: (x, y) not in visited and 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) 

        while len(visited) != len(matrix) * len(matrix[0]):
            while isValid(x, y):
                ans.append(matrix[x][y])
                visited.add((x,y))
                y += 1

            x += 1
            y -= 1
         
            while isValid(x, y):
                ans.append(matrix[x][y])
                visited.add((x,y))
                x += 1

            y -= 1
            x -= 1

            while isValid(x, y):
                ans.append(matrix[x][y])
                visited.add((x,y))
                y -= 1

            x -= 1
            y += 1

            while isValid(x, y):
                ans.append(matrix[x][y])
                visited.add((x,y))
                x -= 1
            
            y += 1
            x += 1
        
        return ans

        