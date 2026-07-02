class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dummy = []
        length = 0

        for i in s:
            if i in dummy:
                index = dummy.index(i)
                dummy = dummy[index + 1:]
            
            dummy.append(i)
            length = max(length, len(dummy))
        return length
        