# https://leetcode.com/problems/longest-increasing-subsequence
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        pile = []
        for n in nums:
            if len(pile) == 0 or pile[-1] < n:
                pile.append(n)
            else:
                ind = bisect_left(pile, n)
                pile[ind] = n
        return len(pile)
    
# a = Solution()
# print(a.lengthOfLIS([6, 3, 5, 10, 11, 2, 9, 14, 13, 7, 4, 8, 12]))