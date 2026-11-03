class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        pos = []
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = abs(nums[abs(nums[i]) - 1]) * (-1)
        for j in range(len(nums)):
            if nums[j] > 0:
                pos.append(j + 1)
        return pos