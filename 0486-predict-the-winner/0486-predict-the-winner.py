class Solution:
    def solve(self, left, right, nums):
        if left > right:
            return 0
        if left == right:
            return nums[left]

        left_part = nums[left] - self.solve(left+1, right, nums)
        right_part = nums[right] - self.solve(left, right-1, nums)
        
        return max(left_part, right_part)

    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)-1
        return self.solve(0, n, nums) >= 0