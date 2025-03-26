# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        slow = head
        fast = head.next
        count = 1
        while fast and fast.next:
            fast = fast.next
            if fast.next:
                fast= fast.next
            slow = slow.next
            count+=1
        s = slow.next
        slow.next = None
        
        while s:
            temp = s.next
            s.next = slow
            slow = s
            s = temp
        while count:
            count-=1
            if head.val != fast.val:
                return False
            head = head.next
            fast = fast.next
        return True
