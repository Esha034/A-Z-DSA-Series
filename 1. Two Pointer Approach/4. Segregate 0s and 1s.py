1. Brute Force — Create a new array

Idea:
create a new array, put all 0s first, then all 1s.

#code

class Solution:
    def segregate0and1(self, arr):
        
        ans = []

        # Put all 0s
        for num in arr:
            if num == 0:
                ans.append(num)

        # Put all 1s
        for num in arr:
            if num == 1:
                ans.append(num)

        return ans


Time: O(n)
Space: O(n)





2. Better Approach — Count 0s


Idea:
Since there are only 0 and 1, if I know how many zeros exist, I automatically know where the ones should go.

#code

class Solution:
    def segregate0and1(self, arr):

        n = len(arr)
        count_zero = 0

        # Count zeros
        for i in range(n):
            if arr[i] == 0:
                count_zero += 1

        # Put zeros first
        for i in range(count_zero):
            arr[i] = 0

        # Put ones afterwards
        for i in range(count_zero, n):
            arr[i] = 1

        return arr
        
#complexity
Time: O(n)
Space: O(1)









3. Better — Two Pointers

Idea:

class Solution:
    def segregate0and1(self, arr):
        i=0
        n=len(arr)
        for j in range(n):
            if arr[j]==0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
        return arr

4. Optimal — Two Pointers

#code
class Solution:
    def segregate0and1(self, arr):

        left = 0
        right = len(arr) - 1

        while left < right:

            while left < right and arr[left] == 0:
                left += 1

            while left < right and arr[right] == 1:
                right -= 1

            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        return arr

#complexity
Time O(n) 
Space-O(1) .
