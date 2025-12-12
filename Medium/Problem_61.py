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
        tail = head

        while tail.next:
            tail = tail.next
            length += 1
        
        tail.next = head
        k %= length
        current = head
        for _ in range(length - k - 1):
            current = current.next
        newHead = current.next
        current.next = None
        return newHead