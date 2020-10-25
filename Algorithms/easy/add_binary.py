# Runtime: 36 ms, faster than 47.16% of Python3 online submissions for Add Binary.
# Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Add Binary.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        res=""
        while a or b:
            ab = int(a[-1]) if a else 0
            a = a[:-1] if a else None
            bb = int(b[-1]) if b else 0
            b = b[:-1] if b else None

            if ab and bb:
                aabb = '1' if carry else '0'
                res = aabb + res
                carry = True
            elif ab or bb:
                if carry:
                    aabb = '0'
                    carry = True
                else:
                    aabb = '1'
                    carry = False
                res = aabb + res
            else:
                aabb = '1' if carry else '0'
                res = aabb + res
                carry = False

        if carry:
            res = '1' + res

        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary('1010','1011'))
    print(sol.addBinary('11','1'))
    print(sol.addBinary('1','0'))
    print(sol.addBinary('0','0'))







