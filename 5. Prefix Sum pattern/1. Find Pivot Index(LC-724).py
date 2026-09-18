class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        left=0
        totalsum=sum(nums)

        for i in range(n):
            right=totalsum-nums[i]-left
            if left==right:
                return i
            left+=nums[i]
        return -1
