class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dup = set()

        for k in nums:
            if k not in dup:
                dup.add(k)
            else:
                return True

        return False