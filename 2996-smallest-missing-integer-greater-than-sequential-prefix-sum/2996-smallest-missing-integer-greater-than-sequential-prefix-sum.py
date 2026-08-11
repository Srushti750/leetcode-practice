class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        number = nums[0]

        for i in range(1, len(nums)):
            if (nums[i-1]+1) != nums[i]:
                break
            number = number + nums[i]
        
        while True:
            if number not in nums:
                nums.append(number)
                break
            number += 1
        return number
        