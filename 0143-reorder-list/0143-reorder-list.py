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
        # Base case: if list has only one node, no reordering needed
        if not head.next: 
            return head
            
        # Step 1: Find the middle of the linked list using two pointers
        # 'first' moves 2 steps, 'second' moves 1 step
        # When 'first' reaches end, 'second' will be at middle
        first = head 
        second = head 
        prev = None  # Keep track of node before 'second' to split the list
        
        while first and first.next: 
            first = first.next.next    # Move 2 steps
            prev = second              # Store current 'second' as previous
            second = second.next       # Move 1 step

        # Step 2: Split the list into two halves
        # Put all nodes from second half into a stack (LIFO order)
        stack = []
        prev.next = None  # Cut the connection between first and second half

        while second: 
            stack.append(second)
            second = second.next

        # Step 3: Prepare for reordering
        cur = head 
        # Important: Set the last node's next to None to avoid cycles
        stack[0].next = None  # stack[0] is the last node of original second half

        # Step 4: Reorder by alternating between first half and second half (from stack)
        # Pattern: 1st -> last -> 2nd -> 2nd_last -> 3rd -> 3rd_last...
        prev = None
        while cur.next and stack:
            nxt = cur.next              # Save next node from first half
            cur.next = stack.pop()      # Connect current to last node from second half
            cur.next.next = nxt         # Connect the popped node back to first half
            cur = nxt                   # Move to next node in first half
        
        # Step 5: Handle remaining nodes from stack (if second half was longer)
        # This happens when the list has odd length and second half has one extra node
        while cur and stack:
            cur.next = stack.pop()      # Attach remaining nodes from stack
            cur = cur.next              # Move to the attached node