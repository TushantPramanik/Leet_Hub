class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in nums.copy():
            if i ==0:
                nums.remove(i)
                nums.append(i)
        return        