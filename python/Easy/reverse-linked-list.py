# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        b = head
        if b.next == None:
            return b
        a = b.next
        t = a.next

        head.next = None

        while t != None:
            a.next = b
            b = a
            a = t
            t = t.next
        a.next = b
        return a


# a = Solution()
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n6 = ListNode(6)
# n7 = ListNode(7)
# n8 = ListNode(8)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
# n7.next = n8


# temp = n1

# while temp != None:
#     print(temp.val, end = " ")
#     temp = temp.next
# print()

# temp = a.reverseList(n1)

# while temp != None:
#     print(temp.val, end = " ")
#     temp = temp.next
# print()