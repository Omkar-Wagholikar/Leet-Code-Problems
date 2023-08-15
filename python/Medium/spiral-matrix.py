# https://leetcode.com/problems/spiral-matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        l = []
        while matrix != []:
            # # -->
            l.extend(matrix.pop(0))
            # # \/
            if len(matrix) != 0 and len(matrix[0]) != 0:
                for i in matrix:
                    l.append(i.pop())
            # # <--
            if matrix != [] :
                l.extend(matrix.pop()[::-1])
            # # /\
            if len(matrix) != 0 and len(matrix[0]) != 0:
                for t in range(len(matrix)-1, -1, -1):
                    i = matrix[t]
                    l.append(i.pop(0))
        return l

# a = Solution()
# a.spiralOrder([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]])

# print(a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])

# a.spiralOrder(
#     [
#         [1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12]
#     ]
# )