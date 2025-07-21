# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.p1 = head 

        def recur_check(cur_node): 
            if cur_node:
                if not recur_check(cur_node.next):
                    return False

                if self.p1.val != cur_node.val: 
                    return False

                self.p1 = self.p1.next
            return True

        return recur_check(head)

            