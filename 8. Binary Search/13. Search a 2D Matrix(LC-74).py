class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        low,high=0,(m*n)-1

        while low<=high:
            guess=(low+high)//2
            row=guess//n
            col=guess%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<=target:
                low=guess+1
                 
            else:
                high=guess-1

        return False
