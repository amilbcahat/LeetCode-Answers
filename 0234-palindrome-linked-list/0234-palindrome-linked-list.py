# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow , fast = head , head 

        #Find middle
        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 

        #Reverse Second half 
        prev = None 
        while slow : 
            tmp = slow.next 
            slow.next = prev 
            prev = slow 
            slow = tmp 
        
        #Check for Palindrome
        left , right = head , prev 
        while left and right : 
            if left.val != right.val : 
                return False 
            left = left.next 
            right = right.next 

        return True 
        