"""
I 1
V 5
IV 4
X 10
IX 9
L 50
XL 40
C 100
XC 90
D 500
CD 500
M 1000
CM 900


"""


class Solution:
    def romanToInt(self, s: str) -> int:
        sumof = 0
        ii = 0
        while ii < len(s):
            if s[ii] == 'I':
                if ii < len(s) - 1 and s[ii+1] == 'V':
                    sumof += 4
                    ii += 2
                    continue
                elif ii < len(s) - 1 and s[ii + 1] == 'X':
                    sumof += 9
                    ii += 2
                    continue
                else:
                    sumof += 1
            elif s[ii] == 'V':
                sumof += 5
            elif s[ii] == 'X':
                if ii < len(s) - 1 and s[ii + 1] == 'L':
                    sumof += 40
                    ii += 2
                    continue
                elif ii < len(s) - 1 and s[ii + 1] == 'C':
                    sumof += 90
                    ii += 2
                    continue
                else:
                    sumof += 10
            elif s[ii] == 'L':
                sumof += 50
            elif s[ii] == 'C':
                if ii < len(s) - 1 and s[ii + 1] == 'D':
                    sumof += 400
                    ii += 2
                    continue
                elif ii < len(s) - 1 and s[ii + 1] == 'M':
                    sumof += 900
                    ii += 2
                    continue
                else:
                    sumof += 100
            elif s[ii] == 'D':
                sumof += 500
            elif s[ii] == 'M':
                sumof += 1000
            else:
                return None

            ii += 1
        return sumof


if __name__ == "__main__":
    sol = Solution()
    print('None ', sol.romanToInt("CVtI"))
    print('1 ', sol.romanToInt("I"))
    print('2 ', sol.romanToInt("II"))
    print('3 ', sol.romanToInt("III"))
    print('4 ', sol.romanToInt("IV"))
    print('5 ', sol.romanToInt("V"))
    print('6 ', sol.romanToInt("VI"))
    print('7 ', sol.romanToInt("VII"))
    print('8 ', sol.romanToInt("VIII"))
    print('5 ', sol.romanToInt("IVI"))
    print('56 ', sol.romanToInt("LVI"))
    print('146 ', sol.romanToInt("XCLVI"))
    print('156 ', sol.romanToInt("CLVI"))
    print('9 ', sol.romanToInt("IX"))
    print('1961 ', sol.romanToInt("MCMLXI"))
