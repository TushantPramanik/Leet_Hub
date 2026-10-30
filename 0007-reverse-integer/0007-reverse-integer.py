class Solution:
    def reverse(self, n: int) -> int:
        copy = n
        n = abs(n)
        sum = 0
        x = len(str(n)) - 1

        for i in range(len(str(n))):
            a = (n % 10) * pow(10, x)
            n = n // 10
            sum = sum + a
            x -= 1

        if sum > 2147483647:
            return 0
        elif copy < 0:
            if -sum < -2147483648:
                return 0
            return -sum
        else:
            return sum       