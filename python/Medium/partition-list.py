# https://leetcode.com/problems/partition-list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, target: int) -> ListNode:
        left = ListNode()
        right = ListNode()
        leftTail = left
        rightTail = right
        while head != None:
            if head.val < target:
                leftTail.next = head
                leftTail = leftTail.next
            else:
                rightTail.next = head
                rightTail = rightTail.next
            head = head.next

        leftTail.next = right.next
        rightTail.next = None
        return left.next

a = Solution()
vals = [1,4,3,2,5,2]
x = 3
n1 = ListNode(0)
temp = n1
for n in vals:
    temp.next = ListNode(n)
    temp = temp.next
temp = n1.next
a.partition(temp, 3)
