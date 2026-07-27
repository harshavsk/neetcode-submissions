# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, p_node = head, None
        while curr:
            n_node = curr.next
            curr.next = p_node
            p_node = curr
            curr = n_node
        return p_node