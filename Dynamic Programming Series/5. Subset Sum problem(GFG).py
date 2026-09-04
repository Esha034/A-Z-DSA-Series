#Memoization code

class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        n=len(arr)
        dp={}
        def dfs(i,sum):
            if sum==0:
                return True
            if i==n:
                return False
                
            if (i,sum) in dp:
                return dp[(i,sum)]
                
            skip=dfs(i+1,sum)
            
            take=False
            
            if arr[i]<=sum:
                take=dfs(i+1,sum-arr[i])
                
            dp[(i,sum)]=take or skip
            
            return dp[(i,sum)]
        return dfs(0,sum)
                
# Complexity
Memoization
Time

O(n × target)

Space

O(n × target)   

I define dfs(i, target) as whether it is possible to form the remaining target using elements from index i onward. 
At each element, I have two choices: either include it (if it doesn't exceed the remaining target) or exclude it. 
The recurrence is take OR skip. If the target becomes 0, I've successfully formed the subset, so I return True. 
If I have processed all elements without reaching 0, I return False. I memoize (i, target) to avoid recomputing overlapping subproblems.
        
#Tabulation (Bottom-Up)

class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        
        n=len(arr)
        dp=[[False]*(sum+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=True
            
        for i in range(n-1,-1,-1):
            for t in range(1,sum+1):
                
                skip=dp[i+1][t]
                
                take=False
                
                if arr[i]<=t:
                    take=dp[i+1][t-arr[i]]
                    
                dp[i][t]=take or skip
                
        return dp[0][sum]
        
        
                
I define dp[i][t] as whether it's possible to form the target t using elements from index i onward. I fill the table from bottom to top because each state depends on the next row. 
For every element, I have two choices: skip it (dp[i+1][t]) or take it if it fits (dp[i+1][t-arr[i]]). If either choice is possible, I mark the current state as True.
The final answer is dp[0][target]


#complexity
Time: O(n × target)

Space: O(n × target)




