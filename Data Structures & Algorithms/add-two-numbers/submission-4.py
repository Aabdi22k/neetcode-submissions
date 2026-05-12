# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        carry = None
        while l1 or l2:
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            if carry:
                s = l1.val + l2.val + carry
                carry = None
            else:
                s = l1.val + l2.val
            if s // 10 > 0:
                carry = s // 10
            node.next = ListNode(s % 10)
            node,l1,l2 = node.next,l1.next,l2.next
        
        if carry:
            node.next = ListNode(carry)
        return dummy.next