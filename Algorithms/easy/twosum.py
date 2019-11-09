from typing import (List)


class Solution:
    def twoSum_iter(self, nums: List[int], target: int) -> List[int]:

        lead = 0
        gotit = False
        twoelem = []
        while True and not gotit and lead < len(nums):
            twoelem = [lead]
            lead = lead + 1
            ii = lead
            while ii < len(nums):
                if nums[twoelem[0]] + nums[ii] == target:
                    twoelem.append(ii)
                    gotit = True
                    break
                ii += 1

        if gotit:
            return twoelem
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ahash = {nums[0]: 0}
        ii = 1
        while ii < len(nums):
            if (target - nums[ii]) in ahash:
                return sorted([ii, ahash[target - nums[ii]]])
            ahash[nums[ii]] = ii
            ii += 1
        return []


if __name__ == "__main__":
    mine = Solution()

    print(mine.twoSum(nums=[1, 2, 3], target=3))
    print(mine.twoSum(nums=[1, 2, 3], target=4))
    print( mine.twoSum(nums=[5,2,3], target=5))
    print( mine.twoSum(nums=[5,7,3], target=10))
    print( mine.twoSum(nums=[5,2,3], target=11))
