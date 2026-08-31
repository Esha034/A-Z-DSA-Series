
class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}

        def dfs(i):

            if i == n:
                return 1

            if i > n:
                return 0

            if i in dp:
                return dp[i]

            oneStep = dfs(i + 1)
            twoStep = dfs(i + 2)

            dp[i] = oneStep + twoStep

            return dp[i]

        return dfs(0) 



Time Complexity: O(n)
Space Complexity: O(n)

        
