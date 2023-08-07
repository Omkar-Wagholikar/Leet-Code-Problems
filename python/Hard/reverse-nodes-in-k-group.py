# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseSub(self, curr, size):
        ts = size-1
        temp = curr
        t = curr
        while ts>0 and t != None:
            t = t.next
            ts -=1

        if t == None:
            return (None, None, None)
        
        finRet = t
        
        a = curr

        b = a.next
        if b == None:
            return (a, None, None)

        t = b.next

        a.next = finRet.next
        size-=1
        while size>0:
            b.next = a
            a = b
            b = t
            if t == None:
                break
            t = t.next
            size -=1
        # print(finRet.val, temp.val, b.val)
        return [finRet, temp, b]

    def reverseKGroup(self, head: 'Optional[ListNode]', k: int) -> 'Optional[ListNode]':
                
        g = self.reverseSub(head, k)
        temp = g[0]
        print(g)
        while g[2] != None:
            b1 = self.reverseSub(g[2] ,k)
            if b1[0] != None:
                g[1].next = b1[0]
            g = b1
        return temp
    
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

# temp = a.reverseKGroup(n1, 1)

# while temp != None:
#     print(temp.val, end = " ")
#     temp = temp.next
# print()