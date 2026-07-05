Brute Force Approach

#Idea
a.Create a new array.
b.Store all non-zero elements.
c.Count the number of zeros.
d.Append zeros at the end.
e.Copy back to nums.

#code
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        for num in nums:
            if num!=0:
                temp.append(num)
        while len(temp) < len(nums):
            temp.append(0)
            
        nums[:]=temp

#Complexity
Time: O(n)
Space: O(n)



Optimal Approach (Two Pointers)
# Idea
Instead of using another array,
keep a pointer where the next non-zero element should be placed.
Two Pointers
j → Read Pointer (checks every element)
i → Write Pointer (next position for a non-zero)

#Algorithm
a.Start i = 0.
b.Traverse using j.
c.If nums[j] is non-zero:
d.Swap nums[i] and nums[j].
e.Increment i.
Ignore zeros.

#code
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        n=len(nums)
        l=0
        for r in range(n):
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
#Complexity
Time: O(n)
Space: O(1)
