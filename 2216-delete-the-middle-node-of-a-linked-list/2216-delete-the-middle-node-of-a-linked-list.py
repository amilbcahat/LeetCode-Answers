# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next : 
            return 

        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy.next 
        #Using Turtle , Hare ALgo to reach middle of the Linked list 
        slow , fast = head , head

        while fast and fast.next : 
            #We maintain a prev to do the deletion process 
            prev = slow 
            slow = slow.next 
            fast = fast.next.next 
        
        #Delete the middle element 
        prev.next = slow.next 
        return dummy.next 