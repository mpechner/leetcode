class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Not the goal here :-D print(haystack.find(needle))
        for ii  in range(len(haystack) - len(needle) + 1 ):
            if haystack[ii:].startswith(needle):
                return ii
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("wert11tyu", 't11'))
    print(sol.strStr("wert11", 't11'))
    print(sol.strStr("t11", 't11'))
    print(sol.strStr("t11w", 't11'))
    print(sol.strStr("tt11w", 't11'))
    print(sol.strStr("tT11w", 't11'))
