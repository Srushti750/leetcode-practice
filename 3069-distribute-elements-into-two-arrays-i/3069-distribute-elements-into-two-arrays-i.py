class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        result = []

        # if len(nums) == 1:
        #     return arr1.append(nums[0])

        # if len(nums) == 2:
        #     arr1.append(nums[0])
        #     arr2.append(nums[1])
        #     result = arr1 + arr2
        #     return result

        arr1.append(nums[0])
        arr2.append(nums[1])

        for number in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[number])
            else:
                arr2.append(nums[number])
        
        result = arr1 + arr2
        return result