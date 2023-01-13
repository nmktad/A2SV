class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row, sublist in enumerate(matrix):
            if sublist[len(matrix[0]) - 1] == target:
                return True
            elif sublist[len(matrix[0]) - 1] > target:
                    for val in sublist:
                        if val == target:
                            return True
                    return False
                
        return False
                
        
        
        
        
        
        
        
        
        
#         lptr = 0
#         rptr = ((len(matrix) - 1) * len(matrix[0])) + (len(matrix[0]) - 1)
        
#         lcol = len(matrix[0])
        
#         while lptr != rptr:
#             mptr = lptr + rptr // 2
#             print(lptr, mptr, rptr)
            
#             if matrix[mptr//lcol][mptr%lcol] == target:
#                 return True
#             elif matrix[mptr//lcol][mptr%lcol] > target:
#                 rptr = mptr - 1
#             else:
#                 lptr = mptr + 1
                
#         return False

                