# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        dummy = ListNode(0)
        dummy.next = head

        first , second = dummy , dummy
        while first.next : 
            if n > 0 : 
                first = first.next 
            else : 
                first = first.next 
                second = second.next
            n -= 1
        
        second.next = second.next.next 

        return dummy.next #we return dummy.next because if head is being removed , then it would handle that case 
        #so we cant just return head , as that would still point to deleted node