Brute Force
# Idea (Interview Explanation)

Generate every possible subarray, calculate its sum, 
and whenever the sum equals k, update the maximum length.

#Algorithm
Start every subarray from index i.
Extend it till the end.
Calculate the running sum.
If sum equals k, update the answer

#code
class Solution:
    def longestSubarray(self, nums, k):

        n = len(nums)
        maxi = 0

        for i in range(n):

            total = 0

            for j in range(i, n):

                total += nums[j]

                if total == k:
                    maxi = max(maxi, j - i + 1)

        return maxi

#complexity
Time: O(n²)
We generate every possible subarray.

Space: O(1)




Optimal (Prefix Sum + HashMap) 
#Idea
Suppose Prefix Sum till index i = sum

If there exists a previous prefix sum
sum - k

thenCurrent Prefix Sum - Previous Prefix Sum = k
So,the subarray between those indices has sum k.

#Algorithm
Initialize:
a.prefix_sum = 0
-max_len = 0
-HashMap {}
b.Traverse the array.
c.Add current element to prefix_sum.
d.If prefix_sum == k
-make it max len(from 0 to i).
e.Check whether
-prefix_sum - k  exists in the map.
f.If yes,calculate length and Store the prefix sum only if it is seen for the first time.


#code
class Solution:
    def longestSubarray(self, nums, k):
        n=len(nums)
        pre_sum=0
        map={}
        max_len=0

        for i in range(n):
            pre_sum+=nums[i]

            if pre_sum==k:
                max_len=i+1

            if (pre_sum-k) in map:
                length=i-map[pre_sum-k]
                max_len=max(max_len,length)

            if pre_sum not in map:
                map[pre_sum]=i

        return max_len

#Complexity
Time: O(n)
Each element is processed once.
HashMap lookup is O(1) on average.

Space: O(n)
Stores prefix sums.

                
