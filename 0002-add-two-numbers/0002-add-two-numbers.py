# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:
        value = 0 
        num1 = 0 
        num2 = 0 

        if not l1 and not l2 and not carry: 
            return None

        if l1 != None: 
            num1 = l1.val
            l1 = l1.next

        if l2 != None: 
            num2 = l2.val
            l2 = l2.next 

        value = num1 + num2 + carry 
        carry = 0 
        if value > 9: 
            carry = value // 10 
            value = value % 10 

        node = ListNode(value)
        node.next = self.addTwoNumbers(l1, l2, carry)
        return node 