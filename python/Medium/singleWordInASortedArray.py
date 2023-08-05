class Solution:

    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if nums[-1] != nums[-2]:
            return nums[-1]

        answer = self.s(0, len(nums)-1, nums)
        return nums[answer]
    
    def s(self, a,b, nums):
        mid = (a+b)//2
        if mid +1 <= len(nums)-1:
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return mid
        elif nums[mid] != nums[mid-1]:
            return mid

        if a<b-1:
            left = self.s(a, mid, nums)
            if left is not None:
                return left
            right = self.s(mid+1, b, nums)
            if right is not None:
                return right

a = Solution()
print(a.singleNonDuplicate([3,3,7,7,10,11,11]))