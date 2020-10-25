# Reaility - had not clue.  Tried a divide and conquer that failed badly
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
# Was easiest to understand
# Runtime: 36 ms, faster than 60.86% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.2 MB, less than 99.97% of Python3 online submissions for Sqrt(x).
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x
        last = x/2
        while True:
            cur = (last + x/last)/2
            if math.floor(cur) == math.floor(last):
                return math.floor(last)
            else:
                last = cur


if __name__ == "__main__":
    sol = Solution()
    print(143, ' ', sol.mySqrt(143))
    print(144, ' ', sol.mySqrt(144))
    print(121, ' ', sol.mySqrt(121))
    print(101, ' ', sol.mySqrt(101))
    print(100, ' ', sol.mySqrt(100))
    print(111, ' ', sol.mySqrt(111))
    print(10, ' ', sol.mySqrt(10))
    print(8, ' ', sol.mySqrt(8))
    print(9, ' ', sol.mySqrt(9))
    print(4, ' ', sol.mySqrt(4))
    print(1, ' ', sol.mySqrt(1))
    print(0, ' ', sol.mySqrt(0))
