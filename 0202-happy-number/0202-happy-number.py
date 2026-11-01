class Solution:
    def isHappy(self, n: int) -> bool:
        while n>=10 or n==7:
            sum=0
            while n >0:
                sum+=(n%10)**2
                n//=10
            n=sum
        if n == 1:
            return True
        else:
            return False        