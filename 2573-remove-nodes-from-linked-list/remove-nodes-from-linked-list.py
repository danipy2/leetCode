# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        Dummynode = ListNode(0,head)
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            if stack:
                stack[-1].next = curr
            else:
                Dummynode.next = curr
            stack.append(curr)
            curr = curr.next
        return Dummynode.next