class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row in range(numRows):
            current = [1]
            if row > 0:
                previous = result[row-1]
                for i in range(len(previous)-1):
                    current.append(previous[i]+previous[i+1])
                current.append(1)
            result.append(current)
        return result
