class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new_nums = []

        for i in nums:
            if i not in new_nums:
                new_nums.append(i)

        for i in range(len(new_nums)):
            nums[i] = new_nums[i]

        return len(new_nums)