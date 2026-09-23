class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        zeroes=0
        ones=0
        res=0
        diffmap={}
        for i in range(n):
            if nums[i]==0:
                zeroes+=1
            if nums[i]==1:
                ones+=1

            diff=zeroes-ones

            if diff==0:
                res=max(res,i+1)
            if diff in diffmap:
                length=i-diffmap[diff]
                res=max(res,length)
            else:
                diffmap[diff]=i
        return res


Complexity:

Time: O(n)
Space: O(n)
