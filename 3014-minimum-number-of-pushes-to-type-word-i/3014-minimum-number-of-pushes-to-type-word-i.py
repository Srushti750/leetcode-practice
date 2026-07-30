class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        for ch in range(0, len(word)):
            pushes += (ch//8) + 1
        return pushes