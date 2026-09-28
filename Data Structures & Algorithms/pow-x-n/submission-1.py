class Solution:
    def myPow(self, x: float, n: int) -> float:
        # (x * x)**n//2 = x^n

        # n is negative
        # invert x
        if n < 0:
            x = 1/x
            n = -n

        # positive n
        res = 1
        while n > 0:
            # n is even
            if n % 2 == 0:
                x = x * x
                n = n // 2
            # n is odd
            else:
                res = res * x 
                n -= 1
        return res
            



