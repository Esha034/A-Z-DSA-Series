Approach 1: Brute Force

# Idea 
I check every possible pair of elements. 
If their sum equals the target, I return their indices.

#Algorithm
Pick the first element.
Pair it with every element after it.
If their sum equals target, return their indices.

#Code
class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):

                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
#Complexity
Time: O(n²)
Every element is compared with every other element.

Space: O(1)
No extra data structure is used.







Approach 2: Better (HashMap)

#Idea
For every element, I calculate the number needed to reach the target (target - current).
If that number is already present in the HashMap, I have found the answer.
Otherwise, I store the current number and its index.

#code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        map={}
        for i in range(n):
            temp=target-nums[i]
            if temp in map:
                return (map[temp],i)
            else:
                map[nums[i]]=i
                
#Complexity

Time: O(n)
We traverse the array once.
HashMap lookup takes O(1) on average.

Space: O(n)
HashMap stores visited elements.





Approach 2: optimal (Two pointer)

#code
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l,r=0,n-1
        while l<r:
            total=numbers[l]+numbers[r]
            if total==target:
                return [l+1,r+1]
            elif total>target:
                r-=1
            else:
                l+=1

Time: O(n)
apce comeplxity: O(1)
