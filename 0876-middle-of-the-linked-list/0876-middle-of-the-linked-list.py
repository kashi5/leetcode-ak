# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=head
        p2=head.next
        while p2 is not None:
            p1=p1.next
            if p2.next is not None:
                p2=p2.next.next if p2.next.next is not None else None
            else:
                p2 = None
        
        return p1
            
            
        