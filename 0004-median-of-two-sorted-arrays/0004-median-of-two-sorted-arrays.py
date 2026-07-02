class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        a = len(nums1)
        b = len(nums2)
        low = 0
        high = a

        while low <= high:
            divide_a = (low + high) // 2
            divide_b = (a + b + 1) // 2 - divide_a

            # for 'a'
            if divide_a == 0:
                left_a = float('-inf')
            else:
                left_a = nums1[divide_a - 1]

            if divide_a == a:
                right_a = float('inf')
            else:
                right_a = nums1[divide_a]

            # for 'b'
            if divide_b == 0:
                left_b = float('-inf')
            else:
                left_b = nums2[divide_b - 1]

            if divide_b == b:
                right_b = float('inf')
            else:
                right_b = nums2[divide_b]

            if left_a <= right_b and left_b <= right_a:
                if (a + b) % 2 == 0:
                    return (max(left_a, left_b) + min(right_a, right_b)) / 2.0
                else:
                    return float(max(left_a, left_b))
            elif left_a > right_b:
                high = divide_a - 1
            else:
                low = divide_a + 1

        