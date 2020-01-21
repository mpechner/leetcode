import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        xx = re.search(r"\s?(\w+)\s*$", s)
        if not xx:
            return 0
        print(xx.groups())
        yy = len(xx.group(1))
        return yy

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord(" foobar  "))
    print(sol.lengthOfLastWord("  foo  bar"))
    print(sol.lengthOfLastWord("foobar"))
    print(sol.lengthOfLastWord(""))
    print(sol.lengthOfLastWord(" "))
    print(sol.lengthOfLastWord(" w "))
