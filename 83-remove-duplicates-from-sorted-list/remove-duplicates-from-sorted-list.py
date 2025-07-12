# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101,head)
        curr = dummy
        temp = curr
        while curr:
            if curr.val!=temp.val:
                temp.next = curr
                temp = temp.next
            else:
                curr = curr.next
        temp.next = None
        return dummy.next