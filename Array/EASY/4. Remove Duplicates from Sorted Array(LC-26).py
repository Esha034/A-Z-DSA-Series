#Approach
1.Keep the first element (it's always unique).
2.Start i = 0.
3.Traverse from j = 1.
4.If nums[j] != nums[i]
5.Found a new unique element.
6.Move i one step ahead.
7.Copy nums[j] to nums[i].
8.Return i + 1.


#intuition

Since the array is sorted, all duplicate values are adjacent. 
I use two pointers. The left pointer points to the last unique element, while the right pointer scans the array. 
If the current right element is different from the left element, it is a new unique value.
I increment the left pointer and copy the new unique value to that position. 
After scanning the entire array, the first l + 1 positions contain all unique elements, so I return l + 1.


#code
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

#Complexity
Time: O(n) (one traversal)
Space: O(1) (in-place)
