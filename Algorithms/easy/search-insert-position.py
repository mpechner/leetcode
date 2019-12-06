from typing import (List)

class Solution:
    def searchInsert_real(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)


    def searchInsert(self, nums: List[int], target: int) -> int:
        for ii in range(0,len(nums)):
            if nums[ii] >= target:
                return ii
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))
    print(sol.searchInsert([1,3,5,6], 2))
    print(sol.searchInsert([1,3,5,6], 7))
    print(sol.searchInsert([1,3,5,6], 0))
