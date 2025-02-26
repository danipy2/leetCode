# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        p1 = dummy
        p2 = dummy.next
        count = 0
        count1 = 0
        while p2:
            count+=1
            p2 = p2.next
        while p1 and count1 < count-n:
            p1= p1.next
            count1+=1
        if p1:
            p1.next = p1.next.next
        return dummy.next
            