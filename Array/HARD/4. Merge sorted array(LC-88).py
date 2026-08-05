#Approach 1 — Brute Force


Idea
Copy all elements of nums2 into the empty positions of nums1.
Sort nums1.

#code
class Solution:
    def merge(self, nums1, m, nums2, n):

        # Copy nums2 into the empty positions of nums1
        for i in range(n):
            nums1[m + i] = nums2[i]

        # Sort the complete array
        nums1.sort()

Complexity
O((m+n)log(m+n))
	​






#Approach 2 — Better Approach Using an Extra Array


Idea:
use two pointer:
i → pointer for valid elements of nums1
j → pointer for nums2
merged → temporary result array

#code
class Solution:
    def merge(self, nums1, m, nums2, n):

        i = 0
        j = 0

        merged = []

        # Compare elements from both arrays
        while i < m and j < n:

            if nums1[i] <= nums2[j]:

                merged.append(nums1[i])
                i += 1

            else:

                merged.append(nums2[j])
                j += 1

        # Add remaining elements from nums1
        while i < m:

            merged.append(nums1[i])
            i += 1

        # Add remaining elements from nums2
        while j < n:

            merged.append(nums2[j])
            j += 1

        # Copy the merged result into nums1
        for index in range(m + n):

            nums1[index] = merged[index]


Complexity
# Every element is processed once:
Time Complexity=O(m+n)
# The temporary array can store m+n elements:
Space Complexity=O(m+n)





#Approach 3 — Optimal In-Place Approach 


Idea:
Since both arrays are already sorted, I use three pointers starting from the end. 
The first pointer points to the last valid element of nums1, the second pointer points to the last element of nums2, and the third pointer points to the last position of nums1.
I compare the elements at the first two pointers and place the larger element at the third pointer. 
Then I move the corresponding pointer backward. Merging from the end prevents overwriting unprocessed elements in nums1.
After the comparison loop, I copy any remaining elements from nums2.

#code
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Last valid element in nums1
        i=m-1
       # Last element in nums2
        j=n-1
      # Last position of nums1
        k=m+n-1
        while i>=0 and j>=0:
            if nums2[j]>nums1[i]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
            k-=1
        # Copy remaining elements of nums2
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1

#Complexity
Time Complexity=O(m+n)
Auxiliary Space Complexity=O(1)
	​
