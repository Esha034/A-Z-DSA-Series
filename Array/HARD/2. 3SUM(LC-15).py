Brute Force
#Idea (Interview Explanation)
Generate every possible triplet using three nested loops. 
If the sum is 0, store the triplet. Since duplicate triplets are possible,
sort each triplet and store it in a set.

#Algorithm
a.Generate all triplets.
b.Check if their sum is 0.
c.Sort the triplet.
d.Insert it into a set.
e.Convert the set into a list.

#Code
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if nums[i] + nums[j] + nums[k] == 0:

                        temp = sorted([nums[i], nums[j], nums[k]])
                        ans.add(tuple(temp))

        return [list(x) for x in ans]
#Complexity
Time: O(n³)
Three nested loops generate all triplets.

Space: O(no. of unique triplets)
Set stores unique triplets.





  
Better (Sorting + HashSet)
  
#Idea (Interview Explanation)
Fix one element. Now the problem becomes finding two numbers whose sum equals -nums[i].
I use a HashSet to solve the remaining Two Sum problem.

#Algorithm
a. Fix one element.
b. Create a HashSet.
c. Traverse remaining elements.
d.Compute:
third = -(nums[i] + nums[j])
e.If third exists in the set:
-We found a triplet.
-Store it in a set to avoid duplicates.
  
#Code
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = set()

        for i in range(n):

            seen = set()

            for j in range(i + 1, n):

                third = -(nums[i] + nums[j])

                if third in seen:
                    temp = sorted([nums[i], nums[j], third])
                    ans.add(tuple(temp))

                seen.add(nums[j])

        return [list(x) for x in ans]
#Complexity
Time: O(n² log m)
Outer loop: n
Inner loop: n
Sorting each triplet (constant size = 3) is effectively constant.
Overall commonly written as O(n²).

Space: O(n)
HashSet for each iteration.








  


Optimal (Sorting + Two Pointers) 
#Idea 

First, sort the array.
Fix one element,
use two pointers(j,k) to find the remaining two numbers 
whose sum = -nums[i].
Since the array is sorted, I can move the pointers efficiently and skip duplicates.

#code
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==0:
                    res.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif total< 0:
                    j+=1
                else:
                    k-=1
        return res
      
#Complexity
Time: O(n²)

Sorting takes O(n log n).
The outer loop runs n times.
The two pointers together move at most n steps for each fixed i.
Hence, the dominant complexity is O(n²).

Space: O(1) (excluding the output list)

We only use pointers and a few variables.
  
