from typing import (List)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curpos=0
        ii=0
        while ii < len(nums):
            if nums[ii] == val:
                ii += 1
                continue
            if ii == curpos:
                ii +=1
                curpos += 1
                continue
            nums[curpos] = nums[ii]
            curpos += 1
            ii += 1
        print(curpos, nums)
        return curpos

if __name__ == "__main__":
    sol = Solution()

    nums = [5,2,2,5]
    length = sol.removeElement(nums, 5)

    nums = [5,4,3,6,4,5,6,3,2,4,6,9]
    length = sol.removeElement(nums, 5)

    nums = [4,3,6,4,5,6,3,2,4,6,9]
    length = sol.removeElement(nums, 5)

    nums = [4,3,6,4,5,6,3,2,4,6,9,5]
    length = sol.removeElement(nums, 5)

    nums = [5]
    length = sol.removeElement(nums, 5)

    nums = [5,5]
    length = sol.removeElement(nums, 5)

    nums = [5,5,3]
    length = sol.removeElement(nums, 5)

    nums = [5,3]
    length = sol.removeElement(nums, 5)
