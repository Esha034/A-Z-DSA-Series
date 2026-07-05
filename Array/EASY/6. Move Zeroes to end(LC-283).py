class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                # Swap the elements
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])
        for i in range(len(temp),n):
            temp.append(0)
        nums[:]=temp
