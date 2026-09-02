

#Memoization approach 

class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def helper(n: int) -> int:
            # Base cases
            if n == 0 or n == 1:
                return n

            # Check if result is already computed and stored
            if n in memo:
                return memo[n]

            # Compute, store in memo, and return
            memo[n] = helper(n - 1) + helper(n - 2)
            return memo[n]

        return helper(n)



#Tabulation approach

class Solution:
    def fib(self, n: int) -> int:

        if n==0 or n==1:
            return n
        
        dp=[-1]*(n+1)
      
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]


#Optimal solution

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        prev2, prev1 = 0, 1
        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1


 Complexity:
Naive Recursion             O(2^n)        O(n)
Memoization (Top-Down)      O(n)          O(n)
Tabulation (Bottom-Up Array) O(n)         O(n)
Iterative Space-Optimized   O(n)          O(1)
