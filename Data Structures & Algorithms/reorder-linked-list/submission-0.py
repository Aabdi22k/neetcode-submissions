# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        l2,slow.next,l1 = slow.next, None, head
        
        prev = None
        curr = l2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        l2 = prev

        dummy = node = ListNode()

        while l1 and l2:
            node.next = l1
            l1 = l1.next
            node = node.next
            node.next = l2
            l2 = l2.next
            node = node.next
            
        node.next = l1 or l2


        
            


        



