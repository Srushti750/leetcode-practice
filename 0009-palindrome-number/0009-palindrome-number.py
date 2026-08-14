class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev = 0
        
        if x < 0:
            return False

        while num != 0:
            rem = num % 10
            rev = rev * 10 + rem
            num = num // 10
        
        return rev == x