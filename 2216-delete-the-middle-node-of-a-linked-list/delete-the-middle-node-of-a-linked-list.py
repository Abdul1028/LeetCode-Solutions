# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next == None:
            return None

        length = 0 
        node = head
        while(node):
            length += 1
            node = node.next
        deleteNode = length //2
        temp = head
        for i in range(0, deleteNode-1):
            temp = temp.next
        temp.next = temp.next.next    
        return head
        
            


        

        