class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitudes =[0]
        length = len(gain)
        for i in range(length):
            alt = altitudes[i]+gain[i]
            altitudes.append(alt)
        maxi = max(altitudes)    
        return maxi   