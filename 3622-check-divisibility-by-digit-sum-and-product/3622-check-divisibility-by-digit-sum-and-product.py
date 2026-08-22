class Solution:
    def checkDivisibility(self, n: int) -> bool:
        i = n
        sum_of_digits = 0
        product_of_digits = 1

        while i > 0:
            digit = i % 10
            i = i // 10
            sum_of_digits += digit
            product_of_digits *= digit
        
        total_sum = sum_of_digits + product_of_digits
        if n % total_sum == 0:
            return True
        return False