from math import floor


class Solution:
    def isPalindrome(self, x: int) -> bool:
        buffer = list(str(x))
        rr = len(buffer)
        if rr <= 1:
            return True
        mid = floor(rr/2)
        if buffer[:mid] == buffer[(-1 * mid):][::-1]:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print('121', sol.isPalindrome(121))
    print('11', sol.isPalindrome(11))
    print('1113111', sol.isPalindrome(1113111))
