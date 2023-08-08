# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: 'Optional[ListNode]', n: int) -> 'Optional[ListNode]':
        if head == None:
            return None
        if head.next == None and n>=1:
            return None
        
        length = n +1
        curr = head
        slow = curr
        while curr != None:
            curr = curr.next
            if length <=0:
                slow = slow.next
            length-=1

        # print("_>", temp)
        if slow == head and length > 0:
            return head.next
        slow.next = slow.next.next
        return head


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

# temp = a.removeNthFromEnd(n1, 2)

# while temp != None:
#     print(temp.val, end = " ")
#     temp = temp.next
# print()