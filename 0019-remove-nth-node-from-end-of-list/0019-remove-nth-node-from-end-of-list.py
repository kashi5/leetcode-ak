# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        current_node = head
        
        while current_node is not None:
            list_len += 1
            current_node = current_node.next
        
        if list_len ==1:
            return None
        
        element_idx = list_len - n
        if element_idx == 0:
            return head.next
        current_node = head
        
        while current_node is not None and element_idx > 1:
            current_node = current_node.next
            element_idx -= 1
        
        current_node.next = current_node.next.next
        return head
        
            
        