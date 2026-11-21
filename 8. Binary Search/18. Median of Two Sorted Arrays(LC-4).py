Bruteforce Approach:
-Merge both arrays, sort them, and find the middle element.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        marr = nums1 + nums2
        marr.sort()

        n = len(marr)
        mid = n // 2

        if n % 2 != 0:
            return float(marr[mid])
        else:
            return (marr[mid - 1] + marr[mid]) / 2


Intuition:

I will first combine both sorted arrays into a single array using concatenation. Then I will sort the merged array in ascending order.

Once the merged array is sorted, I will calculate its length and find the middle index.

There are two possibilities:
- If the total number of elements is odd, the median is the middle element.
- If the total number of elements is even, the median is the average of the two middle elements.
Finally, I will return the median as a floating-point number.
This solution is correct, but it does not satisfy the problems required O(log(m+n))time complexity.














  
Optimal Appproach:
-Use binary search on the smaller array to find the correct partition between the two arrays.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        low, high = 0, m

        while low <= high:
            # Partition positions
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            # Boundary elements
            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == m else nums1[i]

            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == n else nums2[j]

            # Check whether the partition is valid
            if left1 <= right2 and left2 <= right1:

                # Odd total number of elements
                if (m + n) % 2 != 0:
                    return max(left1, left2)

                # Even total number of elements
                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                # Move partition in nums1 to the left
                high = i - 1

            else:
                # Move partition in nums1 to the right
                low = i + 1


Intuition:

I will solve this problem using binary search on the smaller array.

The main idea is to divide both sorted arrays into two halves such that all elements in the left half are smaller than or equal to all elements in the right half.

First, I ensure that binary search is performed on the smaller array to minimize the search space.

I calculate the partition position i in the first array using binary search. Then I calculate the partition position j in the second array so that the left half contains (m + n + 1) // 2 elements.

Next, I identify four boundary elements: the largest elements on the left sides and the smallest elements on the right sides of both arrays.

A partition is valid when left1 is less than or equal to right2 and left2 is less than or equal to right1.

If the partition is valid, I calculate the median. For an odd total length, it is the maximum of the two left boundary elements. For an even total length, it is the average of the maximum left boundary element and minimum right boundary element.

If left1 is greater than right2, I move the partition in the first array to the left. Otherwise, I move it to the right.

The time complexity is O(log(min(m,n))) and the auxiliary space complexity is O(1).


Complexity analysis:
- Time Complexity: (O(log(min(m,n))
- Auxiliary Space Complexity: (O(1))
