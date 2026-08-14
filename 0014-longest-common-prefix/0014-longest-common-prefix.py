class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_list = sorted(strs)
        
        first = sorted_list[0]
        last = sorted_list[-1]
        result = ""
        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result += first[i]
        return result











        # strs.sort()

        # first = strs[0]
        # last = strs[-1]
        # i=0
        
        # while i < min(len(first), len(last)) and first[i]==last[i]:
        #     i += 1
        
        # return first[:i]

