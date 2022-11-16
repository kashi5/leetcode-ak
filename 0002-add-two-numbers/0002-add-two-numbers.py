# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #89+97=186
        #98+79=681
        #999+9=1008
        #999+9=8001
        carry=0
        result = 0
        result_node = ListNode(0)
        result_soln = result_node
        while l1 is not None or l2 is not None:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            result = l1_val + l2_val + carry
            sum_list = result % 10
            carry = result // 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            result_node.next = ListNode(sum_list)
            result_node = result_node.next
        if carry != 0:
            result_node.next = ListNode(carry)
        return result_soln.next
            