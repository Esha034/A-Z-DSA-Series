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


class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        
        n=len(val)
        dp=[[0]*(W+1) for _ in range(n+1)]
        
        
        for i in range(n-1,-1,-1):
            for cap in range(W+1):
                
                skip=dp[i+1][cap]
                
                take=0
                
                if wt[i]<=cap:
                    take=val[i]+dp[i+1][cap-wt[i]]
                    
                dp[i][cap]=max(take,skip)
            
        return dp[0][W]
                    

I define dp[i][cap] as the maximum value obtainable using items from index i onward with remaining capacity cap. I fill the table from the last item to the first because each state depends on the next row (i+1).
The extra row dp[n] is initialized to all zeros, representing the base case where there are no items left to choose from (i == n). For each state, I either skip the current item or take it if it fits, and store the maximum of the two choices.


    
    
3. Optimal: Space Optimized DP approach
