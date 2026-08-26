class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []
        for i in range(0, len(s)):
            if s[i] == '1':
                ones.append(i)
        print(ones)

        shortest_length = float('inf')
        result = ""

        for candidate in range(0, len(ones)-k+1):
            start = ones[candidate]
            end = ones[candidate + k - 1]

            length = end - start + 1
            substring = s[start : end+1]

            if length < shortest_length:
                shortest_length = length
                result = substring
            elif length == shortest_length and substring < result:
                result = substring
        
        return result