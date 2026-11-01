class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_1=set(nums)
        for i in nums_1:
            if nums.count(i)>=len(nums)/2:
                return i
