#code


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m=len(matrix)
        n=len(matrix[0])

        row=m-1
        col=0
        
        while row>=0 and col<=n-1:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                row-=1
            else:
                col+=1
        return False




#Dry run

Input:
matrix = [    [1,  4,  7,  11, 15], 
          [2,  5,  8,  12, 19],    
          [3,  6,  9,  16, 22],   
          [10, 13, 14, 17, 24],   
          [18, 21, 23, 26, 30]]
target = 5



Initially:
row = 4, col = 0



We start at matrix[4][0] = 18.

Dry-run iterations:

Target = 5
Step	Position	Value	Action
1	    (4, 0)	18	18 > 5:  Move up
2	    (3, 0)	10	10 > 5:  Move up
3	    (2, 0)	3	3 < 5:   Move right
4	    (2, 1)	6	6 > 5:   Move up
5	    (1, 1)	5	5 = 5:   Found!

Target found
Return True

Position: row 1, column 1



