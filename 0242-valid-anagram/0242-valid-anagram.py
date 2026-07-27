class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = ""
        string = list(s)

        if len(s) != len(t):
            return False
        for ch in t:
            if ch in string:
                temp = temp + ch
                string.remove(ch)
        if temp == t:
            return True
        else:
            return False