class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)

        for current in range(n+1):
            square = 1
            while (square * square) <= current:
                if dp[current - (square * square)] == False:
                    dp[current] = True
                    break
                square += 1
        return dp[n]