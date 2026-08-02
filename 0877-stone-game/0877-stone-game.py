class Solution:
    def calculate(self, i, j, piles, dp):
        if i>j:
            return 0
        if i==j:
            return piles[i]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        for_i = piles[i] - self.calculate(i+1, j, piles, dp)
        for_j = piles[j] - self.calculate(i, j-1, piles, dp)
        
        dp[i][j] = max(for_i, for_j)

        return dp[i][j]

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[-1] * n for _ in range(n)]
        return self.calculate(0, n-1, piles, dp) >= 0