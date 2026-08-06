class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product_of_digits(num):
            digits = [int(i) for i in str(num)]
            prod = 1
            for i in digits:
                prod = prod * i
            return prod

        temp = n
        while True:
            product = product_of_digits(temp)
            if product % t == 0:
                return temp
            temp = temp+1

        