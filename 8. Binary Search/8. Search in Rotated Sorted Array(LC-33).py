#optimal code
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        low,high=0,n-1

        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]==target:
                return mid
            
            #if we guess on the left half
            if nums[mid]>nums[n-1]:
                if nums[low]<=target<nums[mid]: # Target lies inside the sorted left half
                        high=mid-1
                else:
                        low=mid+1


            #if we guess on the right half
            else:
                if nums[mid]<target<=nums[high]:# Target lies inside the sorted right half
                    low=mid+1
                else:
                    high=mid-1

        return -1
        
        




#better code
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        low,high=0,n-1

        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]==target:
                return mid
            
            #if we guess on the left half
            if nums[mid]>nums[n-1]:
                
                if nums[mid]<target:
                    low=mid+1
                else:
        
                    if nums[low]<=target: # Target lies inside the sorted left half
                        high=mid-1
                    else:
                        low=mid+1


            #if we guess on the right half
            else:
                if target<nums[mid]:
                    high=mid-1
                else:
                    if target<=nums[high]:
                        low=mid+1
                    else:
                        high=mid-1

        return -1
        
        
