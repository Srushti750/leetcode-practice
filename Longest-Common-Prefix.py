1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        strs.sort()
4
5        first = strs[0]
6        last = strs[-1]
7        i=0
8        
9        while i < min(len(first), len(last)) and first[i]==last[i]:
10            i += 1
11        
12        return first[:i]
13
14