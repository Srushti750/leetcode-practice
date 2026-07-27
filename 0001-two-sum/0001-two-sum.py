class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result = []
        # for i in range(0, len(nums)-1):
        #     if(nums[i]+nums[i+1] == target):
        #         result.append(i)
        #         result.append(i+1)
        # return result
        
        result = []
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j] == target):
                    result.append(i)
                    result.append(j)
        return result
