class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a = (high + 1) // 2 - low // 2
        return a