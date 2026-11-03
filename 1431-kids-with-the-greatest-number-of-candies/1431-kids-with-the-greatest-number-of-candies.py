class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(candies)
        bol = []
        for i in candies:
            bol.append(i+extraCandies>=m)
        return bol            