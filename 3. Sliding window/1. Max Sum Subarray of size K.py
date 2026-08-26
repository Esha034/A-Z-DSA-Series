1. Brute Force — O(n × k)

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


I consider every possible subarray of size k. For each subarray, I calculate its sum by iterating over its k elements and keep track of the maximum sum.

Complexity
Time: O(n × k)
Space: O(1)





2. Better — Prefix Sum O(n)

We can precompute the sum up to every index. Then the sum of any subarray can be calculated in O(1).

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

Instead of recalculating each window's sum, I build a prefix-sum array. 
This allows me to calculate every k-sized subarray sum in constant time.

Complexity:

Time: O(n)
Space: O(n)




3. Optimal — Sliding Window

#My code
class Solution:
    def maxSubarraySum(self, arr, k):
        
        n=len(arr)
        if n<k:
            return 0
            
        curr_sum=sum(arr[:k])
        max_sum=float("-inf")
        low,high=0,k-1
        
        while high<n:
            max_sum=max(max_sum,curr_sum)
            low+=1
            high+=1
            if high!=n:
                curr_sum= curr_sum+arr[high]-arr[low-1]
            else:
                break
        return max_sum




Idea:
Since the subarray size is fixed at k, I use a sliding window. I first calculate the sum of the first k elements. 
Then, whenever the window moves one position, I remove the element leaving the window and add the new element entering it.
This avoids recalculating the entire sum.

#optimal code

class Solution:
    def maxSubarraySum(self, arr, k):
        
        n=len(arr)
        low,high=0,k
        curr_sum=0
        max_sum=float("-inf")
        
        for i in range(k):
            curr_sum+=arr[i]
            
        max_sum=curr_sum
            
        for high in range(k,n):
            curr_sum+=arr[high]-arr[low]
            low+=1
            if curr_sum>max_sum:
                max_sum=curr_sum
                
        return max_sum
        
        
Complexity:

Time: O(n)
Space: O(1)
