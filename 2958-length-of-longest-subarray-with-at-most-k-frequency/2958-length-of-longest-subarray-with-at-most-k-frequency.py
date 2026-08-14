from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        longest = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1
            while freq[nums[i]] > k:
                freq[nums[left]] -= 1
                left += 1
            longest = max(longest, i-left+1)
        return longest