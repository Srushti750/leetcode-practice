from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        maximum = 0

        for ch in range(len(s)):
            freq[s[ch]] += 1
            while freq[s[ch]] > 2:
                freq[s[left]] -= 1
                left += 1
            maximum = max(maximum, ch - left + 1)
        return maximum