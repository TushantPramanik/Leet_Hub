class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum=0
        copy=x
        for i in range(len(str(copy))):
            a=x%10
            sum+=a
            x//=10
        if copy%sum==0:
            return sum
        else:
            return -1    