from math import gcd
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def lcm(a, b):
            return a * b // gcd(a,b)

        def count(num):
            cnt = 0
            n = len(coins)

            for subset in range(1, 1<<n):
                current_lcm = 1
                bits = 0
                for i in range(n):
                    if subset & (1<<i):
                        bits += 1
                        current_lcm = lcm(current_lcm, coins[i])

                        if current_lcm > num:
                            break

                if current_lcm > num:
                    continue

                if bits % 2:
                    cnt += num // current_lcm
                else:
                    cnt -= num // current_lcm

            return cnt
        
        left = 1
        right = min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid+1
        return left