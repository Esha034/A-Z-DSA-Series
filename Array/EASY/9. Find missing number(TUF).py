Brute Force (Linear Search)
#Idea 
Since the missing number must lie between 0 and n, I'll check every number in this range. 
For each number, I'll search whether it exists in the array. The number that isn't found is the answer."

#Algorithm
a.Iterate from 0 to n.
b.For each number, search the entire array.
c.If not found, return it.
#Code
class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        for i in range(n+1):
            if i not in nums:
                return i

#Complexity
Time: O(n²)
Space: O(1)





Better (Hashing)
# Idea
Instead of searching every time, I store all numbers in a set.
Set lookup takes O(1), so I can quickly check which number is missing."

#Algorithm
Store all elements in a set.
Check every number from 0 to n.
Return the first missing number.


#code
  class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        s = set(nums)
        for i in range(n + 1):
            if i not in s:
                return i

#Complexity
Time: O(n)
Building the set → O(n)
Checking from 0 to n → O(n)

Space: O(n)
Extra space for the set.






Optimal(Sum Formula)
#Idea 
The sum of numbers from 0 to n is known using a mathematical formula.
If I subtract the actual array sum from the expected sum, 
the remaining value is the missing number.

Formula
Sum=n(n+1)//2

#optimal code
class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=0
        for num in nums:
            actual_sum+=num
            
        return (expected_sum-actual_sum)

#Complexity

Time: O(n)
Only one pass to calculate the array sum.
Space: O(1)
