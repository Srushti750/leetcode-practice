from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        words = Counter(word)
        words = sorted(words.values(), reverse=True)
        pushes = 0
        for i in range(len(words)):
            pushes += words[i] * ((i//8)+1)
        return pushes