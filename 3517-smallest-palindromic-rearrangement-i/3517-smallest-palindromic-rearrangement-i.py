from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        first_half = []
        middle = ""
        result = []
        for ch in sorted(freq):
            first_half.extend(ch*(freq[ch]//2))
            if freq[ch] % 2:
                middle = ch
        first_half = "".join(first_half)
        result = first_half + middle + first_half[::-1]
        return result