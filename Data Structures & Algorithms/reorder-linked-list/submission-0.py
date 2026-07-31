# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half and cut the first half
        second = slow.next
        prev = None
        slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # since second will be None at the end of the whil consider prev
        first,second = head, prev
        # since second half is the small
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2