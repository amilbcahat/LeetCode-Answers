# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        #Neetcode solution
        curr = list1 
        i = 0 
        while i < a - 1: 
            curr = curr.next 
            i += 1 

        head = curr 
        while i <= b : 
            curr = curr.next 
            i += 1 
        head.next = list2

        while list2.next : 
            list2 = list2.next 
        list2.next = curr

        return list1

        #My solution 
        # count = 0 
        # first = list1 
        # while first and first.next and count != (a - 1): 
        #     first = first.next
        #     count += 1 

        # count = 0 
        # second = list1
        # while second and second.next and count != (b): 
        #     second = second.next
        #     count += 1 

        # first.next = list2

        # p1 = list2 
        # while p1 and p1.next: 
        #     p1 = p1.next 

        # p1.next = second.next

        # return list1