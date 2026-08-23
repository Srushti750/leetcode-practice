class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        leftsum = 0
        rightsum = 0
        left = 0
        right = 0

        for i in range(0, mid):
            if num[i] == '?':
                left = left + 1
            else:
                leftsum = leftsum + int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                right = right + 1
            else:
                rightsum = rightsum + int(num[i])

        extra = (right - left) * 9 // 2

        if (left + right) % 2 == 1:
            return True

        result = (leftsum - rightsum) != extra
        return result