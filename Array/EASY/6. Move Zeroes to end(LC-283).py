class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                # Swap the elements
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
