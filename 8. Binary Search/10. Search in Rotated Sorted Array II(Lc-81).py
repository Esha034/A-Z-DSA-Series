class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n=len(nums)
        low,high=0,n-1

        while low<=high:
            guess=(low+high)//2

             # Case 1: Target found
            if nums[guess]==target:
                return True
            # Case 2: Duplicates make the sorted half unclear
            if nums[low]==nums[guess]==nums[high]:
                low+=1
                high-=1
            # Case 3: Left half is sorted
            elif nums[guess]>nums[high]:
                if nums[low]<=target<nums[guess]:
                    high=guess-1
                else:
                    low=guess+1
            # Case 4: Right half is sorted
            else:
                if nums[guess]<target<=nums[high]:
                    low=guess+1
                else:
                    high=guess-1
                    
        return False






        
