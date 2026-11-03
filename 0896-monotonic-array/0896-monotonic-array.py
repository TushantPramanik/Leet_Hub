class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        incr=0
        dec=0
        l=len(nums)
        i=0
        j=1
        while j<l:
            if nums[i] >= nums[j]:
                incr+=1
            if nums[i] <= nums[j]:
                dec+=1
            i+=1
            j+=1
        if incr==l-1 or dec==l-1:
            return True
        else:
            return False            
