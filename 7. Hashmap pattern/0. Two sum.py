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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return (i,j)
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




Initially, I can solve this problem using two nested loops, but that would take O(n²) time.

To optimize it, I use a HashMap to store the elements along with their indices.

I traverse the array once. For each element, I calculate its complement by subtracting the current element from the target.

Then I check whether that complement already exists in the HashMap.

If it exists, I return the index of the complement stored in the HashMap and the current index.

Otherwise, I store the current element as the key and its index as the value.

This way, I can find the required pair in a single traversal, achieving O(n) time complexity
