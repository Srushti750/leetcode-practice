class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
                break
        if count == 0:
            return False
        else:
            return True
