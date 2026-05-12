# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists:
            return self.mergeSort(lists)
        else:
            return None
            
    
    def mergeSort(self, lists):
        if len(lists) > 1:
            mid = len(lists) // 2
            left_half = lists[:mid]
            right_half = lists[mid:]

            left = self.mergeSort(left_half)
            right = self.mergeSort(right_half)
            return self.merge(left, right)

        else:
            return lists[0]
    def merge(self, list1, list2):
        cur = dummy = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1=list1.next
            
            cur = cur.next
        
        cur.next = list1 if list1 else list2

        return dummy.next