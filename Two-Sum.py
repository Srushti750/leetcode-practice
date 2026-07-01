1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        dict = {}
9        for i in range(len(nums)):
10            num = nums[i]
11            sum = target - num
12            if sum in dict:
13                return (dict[sum], i)
14            dict[num] = i
15        return []