class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        final = []
        max_right = -1
        l = len(arr)
        for i in range(l - 1, -1, -1):
            current = arr[i]
            final.append(max_right)
            max_right = max(max_right, current)
        final.reverse()
        return final