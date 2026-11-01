class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums_1=set(nums)
        for i in nums_1:
            if nums.count(i)==1:
                return i
