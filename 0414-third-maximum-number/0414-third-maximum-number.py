class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s = set(nums)
        nums = list(s)
        if len(nums)>=3:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
        else: 
            return max(nums)    