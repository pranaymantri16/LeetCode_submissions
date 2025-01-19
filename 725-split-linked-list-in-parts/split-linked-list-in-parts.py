# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        part_size = length // k
        temp = length % k
        result = []
        current = head
        for i in range(k):
            part_head = current
            lg = part_size + (1 if i < temp else 0)
            for _ in range(lg - 1):
                if current:
                    current = current.next
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            result.append(part_head)
        while len(result) < k:
            result.append(None)
        return result
