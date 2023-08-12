# https://leetcode.com/problems/unique-paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        nums = [1] * (m + n -1)
        tf = self.fact(nums, m+n-2)
        rf = self.fact(nums, m-1)
        lf = self.fact(nums, n-1)
        return tf // (rf * lf)
    
    def fact(self, nums, val):
        if nums[val] > 1:
            return nums[val]
        if val == 1 or val == 0:
            return 1
        nums[val] = val * self.fact(nums, val-1)
        return nums[val]
a = Solution()
a.uniquePaths(10,0)

# # Solution 2: 
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         numCol = m
#         numRow = n
#         grid = []
#         for row in range(numRow):
#             grid.append([0] * numCol)
#         for i in range(numCol):
#             grid[0][i] = 1
#         for i in range(numRow):
#             grid[i][0] = 1
        
#         for row in range(1, numRow):
#             for col in range(1, numCol):
#                 if grid[row][col] == 1:
#                     grid[row][col] = -12
#                     continue
#                 if grid[row][col-1] != -12:
#                     grid[row][col] += grid[row][col-1] 
#                 if grid[row-1][col] != -12:
#                     grid[row][col] += grid[row-1][col] 

#         # for n in grid:
#         #     print(n)
#         return grid[numRow-1][numCol-1]