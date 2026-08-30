#Optimal code

class Solution:
    def longestOnes(self, nums, k):
        low = 0
        zeros = 0
        maxlen = 0

        for high in range(len(nums)):

            if nums[high] == 0:
                zeros += 1

            while zeros > k:

                if nums[low] == 0:
                    zeros -= 1

                low += 1

            curr_len = high - low + 1

            if curr_len > maxlen:
                maxlen = curr_len


# Complexity
Time: O(n)
Space: O(1)
        return maxlen
