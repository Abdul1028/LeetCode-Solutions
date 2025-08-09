# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        slowprev = None

        if head.next == None:
            return None
        while fast and fast.next:
            slowprev = slow
            slow = slow.next
            fast = fast.next.next
        slowprev.next = slowprev.next.next
        return head

            


        

        