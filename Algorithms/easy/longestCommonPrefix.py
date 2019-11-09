from typing import (List)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ''
        ii = 0
        while True:
            try:
                test = strs[0][ii]
                for ll in strs:
                    if ll[ii] != test:
                        return prefix
                prefix += test
                ii += 1
            except Exception:
                break
        return prefix


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(['aal', 'aaa']))
    print(sol.longestCommonPrefix(['flower', 'flow', 'flight']))
    print(sol.longestCommonPrefix(['flower', 'glow', 'flight']))
