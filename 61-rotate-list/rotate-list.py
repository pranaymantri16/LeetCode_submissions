# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        current.next = head
        k = k % length
        h = length - k
        nt = head
        for _ in range(h - 1):
            nt = nt.next
        nh = nt.next
        nt.next = None
        return nh
