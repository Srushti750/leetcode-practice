class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]
        for i in stones:
            count[i%3] += 1
        
        count0, count1, count2 = count

        if count0 % 2 == 0:
            return count1>0 and count2>0
        return abs(count1 - count2) > 2