
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        for mid in range(len(nums)):
            right = total - left - nums[mid]
            if left == right:
                return mid
            left += nums[mid]
        return -1
