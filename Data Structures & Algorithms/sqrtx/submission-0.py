class Solution:
    def mySqrt(self, x: int) -> int:
        L = 1
        R = x

        while L <= R:
            M = (L+R) // 2
            M_squared = M * M

            if M_squared == x:
                return M
            elif M_squared > x:
                R = M - 1
            else:
                L = M + 1
        return R
            