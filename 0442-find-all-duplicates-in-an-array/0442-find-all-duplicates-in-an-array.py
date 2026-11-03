class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = set()
        dup = set()
        for i in nums:
            if i in seen:
                dup.add(i)
            else:
                seen.add(i)
        return list(dup)