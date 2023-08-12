# https://leetcode.com/problems/permutations/description/

class Solution(object):
    def permute(self, nums):
        temp = []
        self.fun(temp, nums, [])
        return temp

    def fun(self, finL:list, a, _stack:list):
        stack = _stack[:]
        b = a[:]
        if len(stack) == len(a):
            finL.append(_stack[:])
            stack.pop()
            return
        
        for i in range(len(a)):
            if b[i] not in stack:
                stack.append(b[i])
                self.fun(finL,a,stack)
                stack.pop()

a = Solution()
print(a.permute([1,2,3,4]))
