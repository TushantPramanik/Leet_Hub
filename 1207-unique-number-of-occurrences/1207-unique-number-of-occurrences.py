class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        uni=set(arr)
        uni=list(uni)
        for i in range(len(uni)):
            for j in range(i+1,len(uni)):
                if arr.count(uni[i]) == arr.count(uni[j]):
                    return False
        return True            

