class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums=set()
        for i in nums1:
            if i in nums2:
                nums.add(i)
        return list(nums)