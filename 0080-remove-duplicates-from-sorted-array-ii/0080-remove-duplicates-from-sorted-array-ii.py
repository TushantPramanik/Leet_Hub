class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums)-1,-1,-1):
            c = nums.count(nums[i])
            if c > 2:
                nums.remove(nums[i])
        ans = len(nums)        
        return ans        