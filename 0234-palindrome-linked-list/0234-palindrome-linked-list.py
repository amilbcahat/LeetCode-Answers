# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #O(n) solution 
        fast = slow = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 

        prev = None
        while slow: 
            tmp = slow.next
            slow.next = prev 
            prev = slow
            slow = tmp 

        left, right = head, prev 
        while left and right: 
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        

        #Recursive Solution (not constant space)
        # self.p1 = head 

        # def recur_check(cur_node): 
        #     if cur_node:
        #         if not recur_check(cur_node.next):
        #             return False

        #         if self.p1.val != cur_node.val: 
        #             return False

        #         self.p1 = self.p1.next
        #     return True

        # return recur_check(head)

            