1. Brute Force — O(n²)

Try every possible starting point and keep extending the subarray until the sum reaches target.


 #code
    
class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        result = n + 1


        for i in range(n):
            curr_sum = 0


            for j in range(i, n):
                curr_sum += nums[j]


                if curr_sum >= target:
                    length = j - i + 1


                    if length < result:
                        result = length


                    break


        if result == n + 1:
            return 0


        return result
        
Idea:
I start a subarray from every possible index and keep adding elements until the sum becomes at least the target. 
Since adding more elements cannot give a shorter subarray for the same starting point, I can stop once the condition is satisfied.

Complexity:

Time: O(n²)
Space: O(1)




2. Prefix Sum + Binary Search


Idea:
This is the O(n log n) follow-up mentioned by LeetCode.

First create a prefix sum array:

nums = [2, 3, 1, 2, 4, 3]


prefix = [0, 2, 5, 6, 8, 12, 15]

For every starting index, we need to find the smallest prefix sum ≥ current prefix + target.

Because all numbers are positive, the prefix array is sorted, so we can use binary search.


#code

class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)


        prefix = [0] * (n + 1)


        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]


        result = n + 1


        for i in range(n):
            required = prefix[i] + target


            low = i + 1
            high = n


            # Binary search
            while low <= high:
                mid = (low + high) // 2


                if prefix[mid] >= required:
                    length = mid - i


                    if length < result:
                        result = length


                    high = mid - 1
                else:
                    low = mid + 1


        if result == n + 1:
            return 0

        return result


Complexity:

Time: O(n log n)
Prefix construction: O(n)
n binary searches: O(n log n)

Space: O(n)









3. Optimal — Sliding Window


#code
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n=len(nums)
        low,high=0,0

        curr_len=0
        min_len=float("inf")
        curr_sum=0

        for high in range(n):
            curr_sum+=nums[high]

            while curr_sum>=target:

                curr_len=high-low+1
                
                if curr_len<min_len:
                    min_len=curr_len
                curr_sum-=nums[low]
                low+=1
        return min_len if min_len!=float("inf") else 0






            


