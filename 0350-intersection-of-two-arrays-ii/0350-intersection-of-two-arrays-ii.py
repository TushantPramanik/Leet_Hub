class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums=[]
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                nums.append(i)
        return nums
