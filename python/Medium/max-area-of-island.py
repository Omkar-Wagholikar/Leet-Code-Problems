# https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: list[list[str]]) -> int:
        marea =0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    marea = max(self.ripple(grid, row, col, 0), marea)
        return marea
    
    def ripple(self, isl, i, j, area):
        a = b = c = d = 0
        if isl[i][j] == 1:
            area += 1
            isl[i][j] = -12
            if i<len(isl)-1:
                a = self.ripple(isl, i+1, j, 0)
            if j<len(isl[0])-1:
                b = self.ripple(isl, i, j+1, 0)
            if 1<=i:
                c = self.ripple(isl, i-1, j, 0)
            if 1<=j:
                d = self.ripple(isl, i, j-1, 0)
            # print(a,b,c,d)
        return area + b + a + c +d
