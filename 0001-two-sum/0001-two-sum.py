class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            sum = target - num
            if sum in dict:
                return (dict[sum], i)
            dict[num] = i
        return []