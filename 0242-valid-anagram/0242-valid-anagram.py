class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # temp = ""
        # string = list(s)

        # if len(s) != len(t):
        #     return False
        # for ch in t:
        #     if ch in string:
        #         temp = temp + ch
        #         string.remove(ch)
        # if temp == t:
        #     return True
        # else:
        #     return False

        dict_s = {}
        dict_t = {}
        
        for ch in s:
            dict_s[ch] = 1 + dict_s.get(ch, 0)
        
        for ch in t:
            dict_t[ch] = 1 + dict_t.get(ch, 0)
        
        if dict_s == dict_t:
            return True
        else:
            return False