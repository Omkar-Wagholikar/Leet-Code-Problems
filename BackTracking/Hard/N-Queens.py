# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solns = []
        self.getSol([], n, solns)
        boards = [self.make_board(i) for i in solns]
        return boards
    
    def check(self, l, n):
        vals = [i+1 for i in range(n)]

        for i in l:
            if i in vals:
                vals.remove(i)

        for i in range(len(l)):
            if l[i] - len(l) +i in vals:
                vals.remove(l[i] - len(l) +i)
        
            if l[i] + len(l) -i in vals:
                vals.remove(l[i] + len(l) -i)
        return vals
    
    def getSol(self, l, n, solns):
        if len(l) == n:
            solns.append(l.copy())
            return
        poss = self.check(l,n)
        if len(poss) == 0:
            return
        else:
            t = l[:]
            for v in poss:
                t.append(v)
                self.getSol(t,n, solns)
                t.pop()

    def make_board(self, l):
        board = []
        for i in range(len(l)):
            vals = "." * (l[i] -1) + "Q" + "." * (len(l) - l[i])
            board.append(vals)
        return board