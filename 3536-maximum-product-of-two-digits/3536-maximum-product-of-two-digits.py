class Solution:
    def maxProduct(self, n: int) -> int:
        digits = list(map(int, str(n)))
        max_num = 0
        i = 0
        while i < len(digits):
            for j in range(i+1, len(digits)):
                temp = digits[i] * digits[j]
                if temp > max_num:
                    max_num = temp
            i = i+1
        return max_num