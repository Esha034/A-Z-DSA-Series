#Optimal code

class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        zeroes=0
        maxlen=0
        currlen=0
        low=0
        
        for high in range(n):

            if nums[high]==0:
                zeroes+=1

            if zeroes>k:
                if nums[low]==0:
                    zeroes-=1
                low+=1
                

            currlen=high-low+1

            if currlen>maxlen:
                maxlen=currlen
        return maxlen


# Complexity
Time: O(n)
Space: O(1)
        return maxlen
