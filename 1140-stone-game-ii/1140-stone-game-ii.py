class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # calculate total remaining stones at each index
        total_remaining = [0] * (n+1)
        for i in range(n-1, -1, -1):
            total_remaining[i] = total_remaining[i+1] + piles[i]

        dp = {}

        def solve(current_index, M):
            if current_index == n:
                return 0
            
            if (current_index, M) in dp:
                return dp[(current_index, M)]

            best = 0
            for X in range(1, 2*M+1):
                if current_index+X > n:
                    break

                # calculate new_M by taking the maximim between current M and X for opponent
                new_M = max(M, X)

                # total stone remaining - opposite score
                current_score = total_remaining[current_index] - solve(current_index+X, new_M)
                best = max(best, current_score)
            
            dp[(current_index, M)] = best
            return best

        return solve(0, 1)