# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: list[int]) -> int:
        lg = len(height)
        l = [height[0]]
        r = [height[-1]]
        count =0
        for i in range(1, lg):
            l.append(max(l[-1], height[i]))
            r.insert(0, max(r[0], height[lg-i-1]))
        for i in range(lg):
            count += min(l[i], r[i]) - height[i]
        return count
    
# height = [4,2,0,3,2,5]
# a = Solution()
# print(a.trap(height))