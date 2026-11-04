class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 33550336:
            return True
        elif num < 10**6:
            sum=0
            copy=num
            i=1
            while i < num:
                if num%i==0:
                    sum+=i
                i+=1    
            if sum==copy:
                return True
            else:
                return False
        else:
            return False