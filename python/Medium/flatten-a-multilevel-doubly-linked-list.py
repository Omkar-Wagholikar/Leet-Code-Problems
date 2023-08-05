# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = Node
        newHead = head
        while(head != None):
            if head.child != None:
                child = self.merge(head)
                temp = head.next    

                head.next = head.child
                head.next.prev = head
                head.child = None

                child.next = temp
                if temp!= None:
                    temp.prev = child

            print(head.val)
            head = head.next
        return newHead

    def merge(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head = head.child
        while(head.next != None):
            head = head.next
        return head

# n1 = Node(1, None, None, None)
# n2 = Node(2, None, None, None)
# n3 = Node(3, None, None, None)
# n4 = Node(4, None, None, None)
# n5 = Node(5, None, None, None)
# n6 = Node(6, None, None, None)

# n1.next = n2
# n2.prev = n1
# n2.next = n3
# n3.prev = n2
# n2.child = n4
# n4.next = n5
# n5.prev = n4
# n4.child = n6
# a = Solution()
# a.flatten(n1)