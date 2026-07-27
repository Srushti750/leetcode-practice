class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                product = (nums[i]-1)*(nums[j]-1)
                if (product > max_product):
                    max_product = product
        
        return max_product