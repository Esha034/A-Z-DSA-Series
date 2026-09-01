Compute dfs(1,0)
Capacity

0

1. Bruteforce: Memoization (Top-Down DP approach)

class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n=len(val)
        dp={}
        
        def dfs(i,W):
            
            if i==n:
                return 0
                
            if (i,W) in dp:
                return dp[(i,W)]
                
            skip=dfs(i+1,W)
            
            take=0
            
            if wt[i]<=W:
                take=val[i]+dfs(i+1,W-wt[i])
                
            dp[(i,W)]=max(take,skip)
            
            return dp[(i,W)]
            
        return dfs(0,W)


2. Better: Tabulation ( Bottom-Up DP approach)

3. Optimal: Space Optimized DP approach
