from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_rows = defaultdict(set)
        for r, v in reservedSeats:
            reserved_rows[r].add(v)

        print(reserved_rows)
        
        # result = 0
        # If a particular row is not in reserved rows that means 4 seats are available
        result = (n - len(reserved_rows)) * 2

        for values in reserved_rows.values():
            left = True
            for i in [2,3,4,5]:
                if i in values:
                    left = False
                    break
            middle = True
            for i in [4,5,6,7]:
                if i in values:
                    middle = False
                    break
            right = True
            for i in [6,7,8,9]:
                if i in values:
                    right = False
                    break
            print(left, middle, right)
            # Case 1: If both left and right is true then 4 seats are available
            if left and right:
                result += 2
            # Case 2: Either one of two is true then 4 seats are available
            elif left or right:
                result += 1
            # Case 3: if neigther left or right is true then check middle
            elif middle:
                result += 1

        return result