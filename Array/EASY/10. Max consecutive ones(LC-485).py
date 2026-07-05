Optimal Approach
#Idea (Interview Explanation)

I traverse the array once. If I see a 1, I increase the current consecutive count.
If I see a 0, I reset the count to 0. 
During the traversal, I continuously update the maximum count.

#Algorithm
a.Initialize:
-count = 0
-maxcount = 0
b.Traverse the array.
c.If the element is 1:
-count += 1
d.Else (0):
-count = 0
e.Update maxcount.
f.Return maxcount.

#code
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        max_count,count=0,0
        for num in nums:
            if num==1:
                count+=1
                max_count=max(max_count,count)
            else:
                count=0
        return max_count

#Complexity
Time: O(n)
We visit each element exactly once.

Space: O(1)
Only two variables (count and maxcount) are used.

