# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        r = 0
        l = 0 
        DummyNode = ListNode(1,head)
        l1 = DummyNode
        r2 = DummyNode
        while r<right:
            if l<left-1:
                l+=1
                l1 = l1.next
            r+=1
            r2 = r2.next
        prev1 = l1.next
        l1.next = r2
        prev = None
        if r2:
            prev = r2.next
        l = prev1
        while right-left >=0:
            left+=1
            nex = l.next 
            l.next = prev
            prev = l
            l = nex
        return DummyNode.next

            


        
