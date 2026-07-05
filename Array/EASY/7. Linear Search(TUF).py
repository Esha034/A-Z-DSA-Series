Optimal approach

#Idea
a.Traverse the array from left to right.
b.Compare each element with the target.
c.If they are equal, return the current index.
d.If the loop finishes and the target is not found, return -1.


#code
class Solution:
    def linearSearch(self, nums, target):
        for i,num in enumerate(nums):
            if num==target:
                return i
        return -1


#Complexity
Time: O(n) (In the worst case, we check every element.)
Space: O(1)
