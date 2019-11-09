class Solution:
    def reverse(self, xx: int) -> int:
        maxint = 2**31
        minint = -1 * (2**31 - 1)
        if xx > maxint or xx < minint:
            return 0
        signed = 1
        if xx < 0:
            signed = -1
            xx = xx * -1
        revint = 0
        while xx > 0:
            revint = revint * 10 + (xx % 10)
            xx = int(xx/10)
        res = signed * revint
        if res > maxint or res < minint:
            res = 0
        return res


if __name__ == '__main__':
    sol = Solution()
    print(321, sol.reverse(321))
    print(654477, sol.reverse(654477))
    print(-654477, sol.reverse(-654477))
