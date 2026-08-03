#Approach 3 (Optimal)
At every step, we maintain the invariant:
1.largest: stores the largest value seen so far.
2.second: stores the second distinct largest value seen so far.
3.Whenever a new maximum is found, the old maximum becomes the
second largest and new maximum becomes the largest.


#Intuition:

 I maintain two variables: largest and second_largest. Initially, largest is the first array element, and second_largest is initialized to negative infinity.
I traverse the array once. If the current element is greater than largest, I move the current largest value into second_largest and update largest.
Otherwise, if the current element is smaller than largest but greater than second_largest, I update second_largest.
The condition num < largest ensures that duplicate occurrences of the largest element are ignored. 
At the end, if second_largest was never updated, I return -1; otherwise, I return it.

#code

class Solution:
    def secondLargestElement(self, nums):

        largest = nums[0]
        second_largest = float('-inf')

        for num in nums:

            # A new largest element is found
            if num > largest:
                second_largest = largest
                largest = num

            # Update the second-largest distinct element
            elif largest > num > second_largest:
                second_largest = num

        # Second-largest distinct element does not exist
        if second_largest == float('-inf'):
            return -1

        return second_largest

#Complexity
Time:O(n)-Only one traversal.
Space:O(1)





#Approach 2 (Better)
1.Find the largest in one pass.
2.Then again traverse the array
3.find the largest element smaller than the maximum.

def secondLargest(nums):
    largest = max(nums)

    second = -1

    for num in nums:
        if num != largest:
            second = max(second, num)

    return second
#Complexity
Time:O(n) + O(n)= O(2n)≈ O(n)
Space: O(1)





# Approach 1 (Brute Force)
1.Sort the array.
2.Largest = last element
3. Now move left from end until you find a different value.

def secondLargest(nums):
    nums.sort()

    largest = nums[-1]

    for i in range(len(nums)-2, -1, -1):
        if nums[i] != largest:
            return nums[i]

    return -1

#Complexity:
Time:Sorting = O(n log n)
Space:O(1) (if sorting in-place)

