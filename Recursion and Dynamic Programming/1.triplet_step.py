class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def solve(idx):
            if idx <= 1:
                return idx
            if idx == 2:
                return 1
            if idx in memo:
                return memo[idx]

            res = solve(idx - 1) + solve(idx - 2) + solve(idx - 3)
            memo[idx] = res
            return res

        return solve(n)


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * 38
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
