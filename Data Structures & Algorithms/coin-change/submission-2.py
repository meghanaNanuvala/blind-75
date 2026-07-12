class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # bottom up, but in reverse order
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

                    # if c = 4, a = 7, dp[7] = 1+dp[3]
        return dp[amount] if dp[amount] != float('inf') else -1


        