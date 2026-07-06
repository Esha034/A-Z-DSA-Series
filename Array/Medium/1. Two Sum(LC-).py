class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return (i,j)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        map={}
        for i in range(n):
            temp=target-nums[i]
            if temp in map:
                return (map[temp],i)
            else:
                map[nums[i]]=i
                
