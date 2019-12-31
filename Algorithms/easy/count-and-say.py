
# took a while to figure out.  over 20 years and not sure I ever had to solve anything like this.
class Solution:
    def cur(self, seq: str) -> str:
        res =''
        thech=''
        numof=0

        for ch in seq:
            if thech == '':
                thech=ch
                numof=1
            elif ch == thech:
                numof += 1
            else:
                res="%s%d%s" %(res,numof,thech)
                thech = ch
                numof = 1

        res = "%s%d%s" % (res, numof, thech)
        return res


    def countAndSay(self, n: int) -> str:
        res = '1'
        n -= 1;
        while n:
            n -= 1;
            res = self.cur(res)

        return res
if __name__ == "__main__":
    sol = Solution()
    for ii in range(1,11):
        print("RES: ",ii, sol.countAndSay(ii))
