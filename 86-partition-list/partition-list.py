class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        bH = ListNode(0)
        aH = ListNode(0)
        b = bH
        a = aH
        C = head
        while C:
            if C.val < x:
                b.next = C
                b = b.next
            else:
                a.next = C
                a = a.next
            C = C.next
        b.next = aH.next
        a.next = None
        return bH.next
