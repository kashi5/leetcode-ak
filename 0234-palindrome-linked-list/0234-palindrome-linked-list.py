# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        reverse_node = self.reverseLL(slow)
        start_node = head
        while start_node is not None and reverse_node is not None:
            if start_node.val != reverse_node.val:
                return False
            start_node = start_node.next
            reverse_node = reverse_node.next
        return True
        
    
    
    def reverseLL(self,node):
        previous_node = None
        current_node  = node
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node
            