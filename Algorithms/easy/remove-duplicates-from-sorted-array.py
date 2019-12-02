from typing import (List)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len = 1
        curpos=0
        for element in nums[1:]:
            print(element)
            if element != nums[curpos]:
                len = len + 1
                curpos += 1
                nums[curpos] = element
        print(len, nums)
        return len
if __name__ == "__main__":
    sol = Solution()
    nums=[1,1,2,3,4,5]
    len = sol.removeDuplicates(nums)
    print("hope 5:", len, nums[0:len] )

    nums = [1, 1]
    len = sol.removeDuplicates(nums)
    print("hope 1:", len, nums[0:len])

    nums = [1]
    len = sol.removeDuplicates(nums)
    print("hope 1:", len, nums[0:len])

    nums = [1,1,1,1,2,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8]
    len = sol.removeDuplicates(nums)
    print("hope 8:", len, nums[0:len])
