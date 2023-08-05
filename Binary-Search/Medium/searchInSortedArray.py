class Solution:
    def search(self, nums: list[int], target: int) -> int:
        answer = self.recursSearch(0, len(nums)-1, nums, target)
        if answer is None:
            return -1
        return answer
    
    def recursSearch(self, st, end, nums, targ):
        mid = (st + end) // 2
        
        if targ == nums[mid]:
            return mid

        if st < end:
            left = self.recursSearch(st, mid, nums, targ)
            if left is not None:
                return left
            right = self.recursSearch(mid +1, end, nums, targ)
            if right is not None:
                return right