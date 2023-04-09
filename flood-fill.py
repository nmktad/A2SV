class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1, 0), (1,0), (0, -1), (0,1)]
        visited = set()

        def floodfill(x, y, color, original):
            if image[x][y] == original:
                # print(f'coloring {x} and {y} original {original} to color {color}')
                image[x][y] = color
                visited.add(tuple([x, y]))
            else:
                return

            for pair in directions:
                newX = x + pair[0]
                newY = y + pair[1]

                if newX >= 0 and newX < len(image) and newY >= 0 and newY < len(image[0]) and tuple([newX, newY]) not in visited:
                    floodfill(newX, newY, color, original)

        if color == image[sr][sc]:
            return image

        floodfill(sr, sc, color, image[sr][sc])

        return image