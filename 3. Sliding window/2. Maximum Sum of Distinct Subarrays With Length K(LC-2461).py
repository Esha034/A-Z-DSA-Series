1. Brute Force

For every possible starting position, calculate the sum of the next k elements from scratch.


#code
class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)

        max_sum = 0

        for i in range(n - k + 1):
            curr_sum = 0

            for j in range(i, i + k):
                curr_sum += arr[j]

            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum


Idea:
I consider every possible subarray of size k. For each subarray, I calculate its sum by iterating over its k elements and keep track of the maximum sum.


Complexity:

Time: O(n × k)
Space: O(1)





2. Better — Prefix Sum 


Idea:

We can precompute the sum up to every index. Then the sum of any subarray can be calculated in O(1).

#code
class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        max_sum = 0

        for i in range(n - k + 1):
            curr_sum = prefix[i + k] - prefix[i]

            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum


Idea:

Instead of recalculating each windows sum, I build a prefix-sum array. This allows me to calculate every k-sized subarray sum in constant time.

Complexity:

Time: O(n)
Space: O(n)




3. Optimal — Sliding Window


#code
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        low,high=0,k
        curr_sum=0
        max_sum=float("-inf")

        freq={}

        for i in range(high):
            freq[nums[i]]=freq.get(nums[i],0)+1
            curr_sum+=nums[i]

        if len(freq)==k:
            max_sum=curr_sum

        for high in range(k,n):

            
            freq[nums[high]]=freq.get(nums[high],0)+1
            curr_sum+=nums[high]-nums[low]

            freq[nums[low]]-=1

            if freq[nums[low]]==0:
                del freq[nums[low]]
            low+=1

            # Check if all elements are distinct
            if len(freq)==k:
                if curr_sum>max_sum:
                    max_sum=curr_sum

        return max_sum if max_sum!=float("-inf") else 0
            

Complexity:

Time: O(n)
Space: O(1)        

#code
