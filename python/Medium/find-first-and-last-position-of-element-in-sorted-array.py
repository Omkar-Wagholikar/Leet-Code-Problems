# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        size = len(nums)
        left, right = self.bisect_left(nums, size, target), self.bisect_rights(nums, size, target)
        if left >=0 and left < size and nums[left] == target and right >=0 and right < size and nums[right] == target:
            return [left, right]
        else:
            return [-1,-1]
    
    def bisect_left(self, nums, len, target):
        low = 0
        high = len
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid
        return low
    
    def bisect_rights(Self, nums, len, target):
        low = 0
        high = len
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid
            else:
                low = mid +1
        return low-1
    
# a = Solution()
# a.searchRange([5,7,7,8,8,10], 8)