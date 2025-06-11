"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Best Optimal approach - 
        if head is None:
            return None  # If the original list is empty, return null

        # Step 1: Create the copied nodes and insert them next to their originals
        current = head
        while current:
            copy = Node(current.val)  # Create a new node (deep copy)
            # original linked list: A->B->C.
            # Updated linked list A->A'->B->B'->C->C.
            copy.next = current.next       # Set the next of the new node
            current.next = copy            # Link the new node after the original node
            current = copy.next            # Move to the next original node

        # Step 2: Assign random pointers for the copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next  # Set the random pointer for the copied node
            current = current.next.next  # Move to the next original node

        # Step 3: Separate the original list from the copied list
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        current = head
        copiedHead = head.next  # Head of the copied linked list
        copy = copiedHead
        while current:
            current.next = current.next.next  # Restore the original list
            if copy.next:
                copy.next = copy.next.next    # Set the next for the copied list
            current = current.next  # Move to the next original node
            copy = copy.next        # Move to the next copied node

        return copiedHead  # Return the head of the copied linked list

        # Easy Approach 
        # oldToCopy = {None: None}

        # cur = head 
        # while cur: 
        #     copy = Node(cur.val)
        #     oldToCopy[cur] = copy
        #     cur = cur.next

        # cur = head 

        # while cur: 
        #     copy = oldToCopy[cur]
        #     copy.next = oldToCopy[cur.next]
        #     copy.random = oldToCopy[cur.random]
        #     cur = cur.next 

        # return oldToCopy[head]