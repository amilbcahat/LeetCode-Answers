# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Same intuition as Find Duplicate Number problem (See Discussions Tab)

        slow , fast = head , head 
        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast : 
                break 
        else: 
            return None #No cycle
        
                
        slow2 = head 

        #This while loop is better , as it checks slow1 != slow2 equality before moving those pointer , hence giving 
        #correct result 
        while slow != slow2 : 
            slow2 = slow2.next 
            slow = slow.next 
        
        return slow2 