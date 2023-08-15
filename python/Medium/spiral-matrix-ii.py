# https://leetcode.com/problems/spiral-matrix-ii
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = []
        for _ in range(n):
            mat.append([0] * n)
        top= 0
        left = 0
        right = n-1
        down = n-1
        start = 1
        while left <= right and top <= down:
            for i in range(left, right+1):
                mat[top][i] = start
                start += 1
            top+=1
            for i in range(top, down+1):
                mat[i][right] = start
                start += 1
            right -=1
            for i in range(right, left-1, -1):
                mat[down][i] = start
                start += 1
            down -=1
            for i in range(down, top-1, -1):
                mat[i][left] = start
                start+=1
            left +=1
        return mat



a = Solution()
mat = a.generateMatrix(3)
for _ in mat:
    print(_)
