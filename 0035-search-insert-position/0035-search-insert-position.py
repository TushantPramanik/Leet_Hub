class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                return i
            elif nums[i]<target:
                return i+1 
            elif nums[0]>target:
                return 0