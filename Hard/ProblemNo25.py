# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        def _reverse(head: ListNode, tail: ListNode) -> ListNode:
            prev = None
            curr = head
            while curr != tail:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev 
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        
        while True:
            kth_node = prev_group_tail
            for _ in range(k):
                if not kth_node.next:
                    return dummy.next
                kth_node = kth_node.next
            curr_group_head = prev_group_tail.next
            next_group_head = kth_node.next
            
            kth_node.next = None 
            new_group_head = _reverse(curr_group_head, None) 
            
            prev_group_tail.next = new_group_head 
            curr_group_head.next = next_group_head 
            
            prev_group_tail = curr_group_head