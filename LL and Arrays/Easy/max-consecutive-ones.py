# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        mcount =0
        count =0
        for n in nums:
            if n == 1:
                count += 1
                if count > mcount:
                    mcount = count
            else:
                if count > mcount:
                    mcount = count
                count = 0
        return mcount

# a = Solution()
# print(a.findMaxConsecutiveOnes([1,0,1,1,0,1]))