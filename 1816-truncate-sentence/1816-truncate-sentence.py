class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()

        for i in range(len(words) - 1, k - 1, -1):
            words.pop(i)

        return " ".join(words)