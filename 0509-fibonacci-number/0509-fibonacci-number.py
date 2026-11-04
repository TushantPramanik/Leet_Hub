class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        else:    
            fib = [0,1]
            x = fib[0]
            y = fib[1]
            for i in range(n-2):
                a=x+y
                fib.append(a)
                x=y
                y=a
            return fib[-1]+fib[-2]    