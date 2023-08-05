# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count =0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count+=1
                    self.ripple(grid, row, col)
        return count
    def ripple(self, isl, i, j):
        if isl[i][j] == "1":
            isl[i][j] = "_"
            if i<len(isl)-1:
                self.ripple(isl, i+1, j)
            if j<len(isl[0])-1:
                self.ripple(isl, i, j+1)

            if 1<=i:
                self.ripple(isl, i-1, j)
            if 1<=j:
                self.ripple(isl, i, j-1)