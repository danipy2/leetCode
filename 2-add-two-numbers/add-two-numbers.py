# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(0,None)
        l = h
        self.add(l1,l2,0,l)
        return h.next

    def add(self,l1,l2,r,l):
        if l1 or l2:
            total = r
            r = 0
            if l1 :
                total+= l1.val
                l1 = l1.next
            if l2 :
                total += l2.val
                l2 = l2.next
            if total>9:
                r = total//10
                total = total %10
            newnode = ListNode(total,None)
            l.next = newnode
            l = l.next
            self.add(l1,l2,r,l)
        else:
            if r:
                newnode = ListNode(r,None)
                l.next = newnode
                l = l.next


       

        