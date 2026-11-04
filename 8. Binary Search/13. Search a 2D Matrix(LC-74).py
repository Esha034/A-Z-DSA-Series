1. Brute-force approach — two nested loops:

#Interview explanation:

“I will traverse the matrix using two nested loops. The outer loop iterates through each row, and the inner loop iterates through each element in that row. I will compare every element with the target. If I find a match, I return True; if I finish traversing the entire matrix without finding it, I return False.”


#Code:


class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True

        return False



#Dry run:

For target = 3:
i (row)	j (column)	matrix[i][j]	Result
0	0	1	Not found
0	1	3	Found → return True

We stop immediately when we find the target.
    
#Complexity:
- Time: \(O(m \times n)\) in the worst case.
- Auxiliary space: \(O(1)\).
The problem is that we may have to inspect every element, even though the matrix is sorted.








2. Better approach — binary search twice

#Interview explanation:

“Since each row is sorted and the first element of each row is greater than the last element of the previous row, I can first use binary search to identify the row where the target could exist. I will then apply binary search again within that row to find the target. This avoids traversing every element.”

The first binary search finds a row satisfying:
\[
matrix[i][0] \le target \le matrix[i][n-1]
\]

If no such row exists, the target is absent.




#Code:

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        # Binary search to find the possible row
        low, high = 0, m - 1
        row = -1

        while low <= high:
            mid = (low + high) // 2

            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        if row == -1:
            return False

        # Binary search inside the identified row
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False



#Dry run:

For target = 3:

First binary search — identify the row

Initially, low = 0, high = 2.
- mid = (0 + 2) // 2 = 1
- Row 1 ranges from 10 to 20.
- Since 3 < 10, search the rows above it: high = 0.
- Now mid = (0 + 0) // 2 = 0.
- Row 0 ranges from 1 to 7. Since 1 <= 3 <= 7, the possible row is row 0.
Second binary search — search within row 0

The row is [1, 3, 5, 7].
- low = 0, high = 3
- mid = 1
- matrix[0][1] = 3, which equals the target.
- Return True.


#Complexity:
- Time: \(O(\log m + \log n)\), which is equivalent to \(O(\log(mn))\).
- Auxiliary space: \(O(1)\).
This is already an efficient solution. The optimal approach below achieves the same asymptotic time complexity with just one binary search.















    
    
3. Optimal approach — binary search on the entire matrix



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



