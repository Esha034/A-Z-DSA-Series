#better

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        low,high=0,n-1
        res=-1
        while low<=high:
            mid=(low+high)//2
            
            if nums[mid]>nums[n-1]:
                low=mid+1
            else:
                res=nums[mid]
                high=mid-1
        return res



#optimal 

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]

        
