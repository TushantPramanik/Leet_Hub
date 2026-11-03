class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        l1=set()
        l2=set()
        final=[]
        for i in nums1:
            if i not in nums2:
                l1.add(i)
        for j in nums2:
            if j not in nums1:
                l2.add(j)      
        l1=list(l1)
        l2=list(l2)
        final.append(l1)
        final.append(l2)  
        return final                