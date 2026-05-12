# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        carry = 0
        while l1 or l2 or carry:

            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0

            s = l1v + l2v + carry
            carry = s // 10

            node.next = ListNode(s % 10)

            node,l1,l2 = node.next,l1.next if l1 else None,l2.next if l2 else None
        
        return dummy.next

