class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num = num * 10 + i
        num = num + 1
        result = list(map(int, str(num)))
        return result