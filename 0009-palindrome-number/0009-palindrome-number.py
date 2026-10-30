class Solution:
    def isPalindrome(self, n: int) -> bool:
        copy=n
        sum=0
        x=len(str(n))-1

        for i in range(len(str(n))):
            a=(n%10)*pow(10,x)
            n=n//10
            sum=sum+a
            x-=1

        if sum==copy:
            return True
        else:
            return False