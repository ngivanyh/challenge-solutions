# Leetcode 50

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        def pow(x: float, n: int):
            if not n:
                return 1

            root = pow(x, n // 2)
            return x * root * root if n & 1 else root * root

        return pow(x, n)