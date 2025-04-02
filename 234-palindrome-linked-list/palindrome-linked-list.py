# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        temp = head
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        prev = None
        while slow:
            n = slow.next
            slow.next = prev
            prev = slow
            slow = n
        while prev and temp:
            if prev.val != temp.val:
                return False
            prev = prev.next
            temp = temp.next
        return True

        
