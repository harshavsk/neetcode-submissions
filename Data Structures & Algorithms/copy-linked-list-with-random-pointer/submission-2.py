"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # duplicate create
        curr = head
        while curr is not None:
            l2 = Node(curr.val)
            l2.next = curr.next
            curr.next = l2
            curr = l2.next
        # generating random
        curr = head
        while curr:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next
        # creating a new one
        newhead = head.next
        curr = head
        while curr:
            l2 = curr.next
            curr.next = l2.next
            if l2.next is not None:
                l2.next = l2.next.next
            curr = curr.next
        return newhead