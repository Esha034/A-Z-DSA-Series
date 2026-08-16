Approach 1 — Brute Force

Idea

Square every element.
Sort the squared array.
Return the result.

#Code
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        # Square every element
        for i in range(n):
            nums[i] = nums[i] * nums[i]

        # Sort the squared array
        nums.sort()

        return nums

Time Complexity=O(nlogn)
Auxiliary Space Complexity=O(1)
	​








Approach 2 — Better Two-Pointer Approach 

Idea:

Since the input array is already sorted, the largest absolute value must be present at either the left end or the right end. 
I use two pointers, one at the beginning and one at the end. I compare the squares of both values and place the larger square at the current last position of the result array.
Then I move the corresponding pointer inward and continue filling the result from right to left. 
This avoids sorting and processes every element only once.

#better Code

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            nums[i] = nums[i] * nums[i]

        l,r=0,n-1
        position=n-1

        while l<=r:
            if nums[l]>nums[r]:
                ans[position]=nums[l]
                l+=1
            else:
                ans[position]=nums[r]
                r-=1
            position-=1
        return ans








Approach 3: Optimal Approach 

Idea:

Because the array is sorted:

[-7, -3, 2, 3, 11]
 ↑                 ↑
left             right

The largest absolute value must be at one of the ends.

Since the input array is sorted, so after squaring the elements, the largest absolute value can only be at either end of the array.
Therefore, I use two pointers, one at the beginning and one at the end. 
I compare their absolute values, square the larger one, and place that square at the current position from the end of the result array.
Then I move the corresponding pointer inward and continue filling the result from right to left. 
Since each element is processed exactly once, the time complexity is O(n)


#code

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
		
        n=len(nums)
        ans=[0]*n
        left,right=0,n-1
		
        for i in range(n-1,-1,-1):
			
            if abs(nums[left])<abs(nums[right]):
                ans[i]=nums[right]*nums[right]
                right-=1
				
            else:
                ans[i]=nums[left]*nums[left]
                left+=1
        return ans


#complexity

Time Complexity=O(n)
Auxiliary Space Complexity=O(n)
