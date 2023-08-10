# https://leetcode.com/problems/kth-missing-positive-number
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        arr.sort()
        length = len(arr)

        if arr[0] > k:
            return k

        k -= (arr[0] -1)

        low = 0
        high = length-1
        while low <= high:
            mid = (high + low) // 2
            if (arr[mid] - arr[0] - mid) < k:
                low = mid + 1
            else:
                high = mid -1
        return arr[low-1] + k -(arr[low-1] - arr[0] - (low-1))
    
# a = Solution()
# a.findKthPositive([5,1,6,8,9,10], 4)
# print(a.findKthPositive([1,2,3,4], 2))
# a.findKthPositive([2,3,4,7,11], 5)