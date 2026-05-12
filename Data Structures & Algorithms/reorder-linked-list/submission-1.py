# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f,s = head, head
        cur = dummy = ListNode()
        while f and f.next:
            s = s.next
            f = f.next.next
        
        l1 = head
        l2 = s.next
        s.next = None

        prev, cur2 = None, l2

        while cur2:
            nxt = cur2.next
            cur2.next = prev
            prev = cur2
            cur2 = nxt

        l2 = prev
        while l1 and l2:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        
        cur.next = l1 if l1 else l2

        head = dummy.next
        