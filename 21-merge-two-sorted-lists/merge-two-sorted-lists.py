# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode(-101,None)
        curr = dummynode
        while list1 or list2:
            val1 = list1.val if list1 else 101
            val2 = list2.val if list2 else 101
            if val1<val2:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return dummynode.next