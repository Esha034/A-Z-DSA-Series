1. Brute Force Using Another Array


#Idea
Create a new array and put an element into it only if it isn't already the last element.


#code
class Solution:
    def removeDuplicates(self, nums):
        
        unique = []
        for num in nums:
            if len(unique) == 0 or unique[-1] != num:
                unique.append(num)

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)

My first approach is to create a separate array to store the unique elements. 
Since the input is sorted, I only need to compare the current element with the last element stored in the unique array.
If they are different, I add the element. Finally, I copy the unique elements back into the original array and return the number of unique elements.

  
Time-O(n) 
Space- O(n) 







Approach 3 — Optimal Two-Pointer Approach

class Solution:
    def removeDuplicates(self, nums):

        n = len(nums)

        left = 0
        right = 1

        while right < n:

            if nums[right] != nums[left]:

                left += 1
                nums[left] = nums[right]

            right += 1

        return left + 1


Since the array is sorted, all duplicate values are adjacent. I use two pointers.
The right pointer scans the array to find new unique elements, while the left pointer keeps track of the position of the last unique element. 
Whenever nums[right] is different from nums[left], I increment left and copy nums[right] to nums[left]. 
At the end, the first left + 1 positions contain all unique elements in sorted order, so I return left + 1.


Time-O(n) 
Space-O(1) 


