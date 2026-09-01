class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def dfs(i):
            if i >=n:
                return 0
            if i in dp:
                return dp[i]
                
            maxamt=nums[i]+max(dfs(i+2),dfs(i+3))
            dp[i]=maxamt
            return maxamt
        return max(dfs(0),dfs(1))


I define dfs(i) as the maximum money that can be collected if I rob house i. After robbing house i, I cannot rob the adjacent house, so the next robbed house can begin from either i+2 or i+3. I recursively compute both possibilities, take the maximum, and memoize the result. Since the first robbed house can be either index 0 or index 1, I return max(dfs(0), dfs(1))

Complexity
Time:
O(n)
Space:
O(n)



#optimal code

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def dfs(i):
            if i >=n:
                return 0
            if i in dp:
                return dp[i]

            take=nums[i]+dfs(i+2)
            skip=dfs(i+1)

            dp[i]=max(take,skip)
            return dp[i]

        return dfs(0)



Complexity:

Time Complexity:
Each index is solved only once.
O(n)

Space Complexity:
DP dictionary: O(n)

Recursion stack (worst case): O(n)

Overall:

O(n)

