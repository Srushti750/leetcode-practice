class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        missing = 0
        for i in range(1, 110):
            number = k * i
            if number not in nums:
                missing = number
                break
        print(missing)
        return missing