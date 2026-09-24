class Solution:
    def myPow(self, x: float, n: int) -> float:
        # case 1: n is negative
        if n < 0:
            x = 1/x
            n = -n

        res = 1.0
        while n > 0:
            # case 2: n is even
            if n % 2 == 0:
                x = x * x
                n = n // 2
            # case 3: n is odd
            else:
                res *= x
                n -= 1
        return res
