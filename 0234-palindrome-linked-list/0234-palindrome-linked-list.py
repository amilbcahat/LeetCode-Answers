# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Stack solution 
        stack = []
        cur = head
        while cur: 
            stack.append(cur.val)
            cur = cur.next 

        cur = head
        while cur and cur.val == stack.pop(): 
            cur = cur.next 

        return cur is None
        # #O(n) solution 
        # #Find middle
        # fast = slow = head
        # while fast and fast.next: 
        #     slow = slow.next
        #     fast = fast.next.next 

        # #Reverse second half
        # prev = None
        # while slow: 
        #     tmp = slow.next
        #     slow.next = prev 
        #     prev = slow
        #     slow = tmp 

        # #Check for pali
        # left, right = head, prev 
        # while left and right: 
        #     if left.val != right.val:
        #         return False
        #     left = left.next
        #     right = right.next

        # return True
        

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

            