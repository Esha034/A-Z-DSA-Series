class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        low,high=0,n-1
        ans1,ans2=-1,-1

        while low<=high:

            mid=(low+high)//2

            if nums[mid]==target:
                ans1=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        

        low,high=0,n-1
        while low<=high:
            
            mid=(low+high)//2

            if nums[mid]==target:
                ans2=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1

        return [ans1,ans2]
        
