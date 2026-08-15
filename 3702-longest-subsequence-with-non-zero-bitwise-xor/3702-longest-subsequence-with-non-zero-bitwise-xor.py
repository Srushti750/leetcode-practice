class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            total = total ^ i
        if total != 0:
            return len(nums)
        for i in nums:
            if i != 0:
                return len(nums)-1
        return 0