# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.front = head
        self.stop = False
        def recur(back): 
            if not back: 
                return 

            recur(back.next)

            if self.stop: 
                return 

            #Reach mid, now dont do anything and return
            if self.front == back or self.front.next == back: 
                back.next = None
                self.stop = True
                return 

            front_next = self.front.next 
            self.front.next = back
            back.next = front_next
            self.front = front_next
            
        recur(head)
        return head
