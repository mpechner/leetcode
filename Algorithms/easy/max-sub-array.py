from typing import (List)

class Solution:
    # Kadane's - did not know about this method. Was not published until I was a Junior in college.
    # https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
    # if you look in pypi - people have done the code - this is either a method,
    # or test of what people remember from algoithms class
    # If they took the class in the early 90's or later.
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        curSum = maxSum = nums[0]

        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(curSum, maxSum)

        return maxSum
    # Mine - brute force
    def maxSubArray2(self, nums: List[int]) -> int:
        maxvalue = nums[0]
        ar_len = len(nums)
        right_range = ar_len + 1
        left = 0
        while left < ar_len:
            right = right_range
            while right > left:
                sumof =sum(nums[left:right])
                maxvalue = max(maxvalue, sumof)
                right   -=1
            left +=1
        return maxvalue
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1]))
    print(sol.maxSubArray([-4]))
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
