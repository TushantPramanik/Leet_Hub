class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        miss = []
        i=0
        while len(miss)<=k+1:
            i+=1
            if i not in arr:
                miss.append(i)
        return miss[k-1]        