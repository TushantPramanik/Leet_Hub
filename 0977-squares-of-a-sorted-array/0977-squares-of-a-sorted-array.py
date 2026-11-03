import numpy as np
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums1 = np.array(nums)
        sq = nums1**2
        sq=sq.tolist()
        sq.sort()
        return sq