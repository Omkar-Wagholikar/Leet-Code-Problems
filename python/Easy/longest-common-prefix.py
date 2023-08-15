# https://leetcode.com/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        soln = ""
        if first == last:
            return first
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return soln
            soln += first[i]
        return soln

a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
