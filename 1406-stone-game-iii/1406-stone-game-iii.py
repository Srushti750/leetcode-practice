class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [None] * n

        def solve(i):
            if i >= n:
                return 0

            if dp[i] is not None:
                return dp[i]
            
            total = 0
            best = float("-inf")

            for k in range(3):
                if i+k < n:
                    total += stoneValue[i+k]
                    best = max(best, total - solve(i+k+1))
            dp[i] = best
            return dp[i]

        diff = solve(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"