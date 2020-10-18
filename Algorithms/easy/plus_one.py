from typing import (List)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ii=len(digits) - 1
        carry = False
        while(ii >= 0):
            carry = False
            xx = digits[ii] + 1
            if xx > 9:
                carry = True
                digits[ii] = 0
            else:
                digits[ii] = xx
            ii -= 1
            if carry and ii >= 0:
                digits[ii] += 1
                carry = False
            if digits[ii] <= 9:
                break

        if carry:
            digits = [1] + digits
        return digits

if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1,9]))
    print(sol.plusOne([9]))
    print(sol.plusOne([3]))
    print(sol.plusOne([9,9]))
