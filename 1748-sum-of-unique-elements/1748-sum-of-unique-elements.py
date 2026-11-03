class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        s=0
        for i in nums:
            if nums.count(i)==1:
                s+=i
        return s       