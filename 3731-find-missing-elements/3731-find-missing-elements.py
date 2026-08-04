class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        smallest = nums[0]
        largest = nums[len(nums)-1]
        result = []

        for i in range(smallest, largest):
            if i not in nums:
                result.append(i)
        return result