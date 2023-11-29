class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []

        for i in range(len(matrix[0])):
            arr.append([])
            for j in range(len(matrix)):
                arr[-1].append(matrix[j][i])
        
        return arr
        