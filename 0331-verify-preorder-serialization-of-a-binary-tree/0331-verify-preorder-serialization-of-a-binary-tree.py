class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Initialize the number of available slots for nodes in the binary tree.
        availableSlots = 1

        # Get the length of the input string.
        length = len(preorder)

        # Traverse through each character in the input string.
        for i in range(length):
            # If a comma is encountered, a new node has been processed.
            if preorder[i] == ',':
                # Decrease the available slots by 1 as the node consumes one slot.
                availableSlots -= 1

                # If no slots are available, the serialization is invalid.
                if availableSlots < 0:
                    return False

                # If the previous character is not '#', it represents a non-null node,
                # which creates two additional slots for its children.
                if preorder[i - 1] != '#':
                    availableSlots += 2

        # Process the last node in the input string.
        availableSlots = availableSlots - 1 if preorder[length - 1] == '#' else availableSlots + 1

        # The serialization is valid if all slots are exactly filled.
        return availableSlots == 0