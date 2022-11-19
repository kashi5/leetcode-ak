# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # return self.solution1(head,n)
        return self.solution2(head,n);
        
        
    def solution2(self,head,n):
        list_1 = head
        list_length = 1
        while list_length <= n:
            list_1 = list_1.next
            list_length += 1
        if list_1 is None:
            if list_length ==2:
                return None
            head.val = head.next.val
            head.next = head.next.next
            return head
        list_2 = head
        while list_1.next is not None:
            list_1 = list_1.next
            list_2 = list_2.next
        list_2.next = list_2.next.next
        return head
        
            
        
    
    
    
    def solution1(self,head,n):
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
        
            
        