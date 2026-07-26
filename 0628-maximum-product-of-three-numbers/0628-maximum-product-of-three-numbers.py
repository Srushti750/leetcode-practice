class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # three largest
        product1 = nums[-1] * nums[-2] * nums[-3]
        # two smallest and one largest
        product2 = nums[0] * nums[1] * nums[-1]

        return max(product1, product2)