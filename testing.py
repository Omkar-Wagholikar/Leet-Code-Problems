# https://leetcode.com/problems/pacific-atlantic-water-flow/
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pass

def display(m):
    for n in m:
        print(n)

def check(h):
    ra = []
    rb = []
    for _ in range(len(h)):
        ra.append([False] * len(h[0]))
        rb.append([False] * len(h[0]))

    ripplea(h, ra, 1, 2)
    print("ra")
    display(ra)
    # print("rb")
    # display(rb)
    
def ripplea(h, ra, row, col):
    if row == 0 or col == 0:
        ra[row][col] = True

    if col > 1 and h[row][col] >= h[row][col-1]:
        print("a")
        if ra[row][col-1] == True:
            ra[row][col] = True
        else:
            ripplea(h,ra, row, col-1)
    if row > 1 and h[row][col] >= h[row-1][col]:
        print("b")
        if ra[row-1][col] == True:
            ra[row][col] = True
        else:
            ripplea(h, ra, row, col)

    if col < len(h[0])-1 and h[row][col] >= h[row][col+1]:
        print("c")
        if ra[row][col+1] == True:
            ra[row][col] = True
        else:
            ripplea(h,ra, row, col+1)

    if row < len(h) -1 and h[row][col] >= h[row+1][col]:
        print("d")
        if ra[row+1][col] == True:
            ra[row][col] = True
        else:
            ripplea(h, ra, row+1, col)

heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
check(heights)