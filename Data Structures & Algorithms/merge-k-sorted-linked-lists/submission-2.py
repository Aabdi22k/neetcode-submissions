# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists:
            while len(lists) > 1:
                l1 = lists.pop()
                l2 = lists.pop()

                l3 = self.merge(l1, l2)
                lists.append(l3)
            
            return lists[0]

            # or use return self.mergeSort(lists)
            # Merge sort will run in O(n log k) time instead of
            # The iterative solution above which is O(n * k)
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