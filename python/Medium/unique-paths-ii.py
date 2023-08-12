# https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return 0
        numCol = len(grid[0])
        numRow = len(grid)
        
        for i in range(numCol):
            if grid[0][i] != 1:
                grid[0][i] = 1
            else:
                for j in range(i, numCol):
                    grid[0][j] = -12
                break

        for i in range(1,numRow):
            if grid[i][0] != 1:
                grid[i][0] = 1
            else:
                for j in range(i, numRow):
                    grid[j][0] = -12
                break
        
        for row in range(1, numRow):
            for col in range(1, numCol):
                if grid[row][col] == 1:
                    grid[row][col] = -12
                    continue
                if grid[row][col-1] != -12:
                    grid[row][col] += grid[row][col-1] 
                if grid[row-1][col] != -12:
                    grid[row][col] += grid[row-1][col] 

        # for n in grid:
        #     print(n)
            
        if grid[numRow-1][numCol-1] != -12:
            return grid[numRow-1][numCol-1]
        else:
            return 0

# a = Solution()
# print(a.uniquePathsWithObstacles(
#     [
#         [1],
#         [0]
#     ]))