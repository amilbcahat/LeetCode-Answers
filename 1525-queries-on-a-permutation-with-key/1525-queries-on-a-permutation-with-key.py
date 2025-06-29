class BIT: 
    def __init__(self, m, queries): 
        # Store number of queries - this tells us how many "front slots" we need to reserve
        self.n = len(queries)
        
        # Create BIT array: size = original_array_size + front_slots + 1
        # Example: m=5, n=4 → size = 5+4+1 = 10
        # Positions 0: unused (BIT is 1-indexed)
        # Positions 1-4: reserved for moved elements (front area)  
        # Positions 5-9: original positions for elements 1,2,3,4,5
        self.bit = [0] * (m + self.n + 1)
        
        # Track current virtual position of each element
        # positions[i] = virtual position where element i currently lives
        self.positions = [0] * (m + 1)

    def getSum(self, index): 
        """
        Calculate prefix sum from position 1 to 'index' in the BIT
        This tells us "how many elements are in positions 1 through index"
        Which equals "how many elements are to the left of position (index+1)"
        """
        # Convert to 1-indexed (BIT uses 1-based indexing)
        index += 1
        res = 0
        
        # Standard BIT traversal to calculate prefix sum
        while index > 0:
            res += self.bit[index]
            # BIT magic: jump to parent node in the tree
            # This skips unnecessary positions for efficiency
            index -= index & -index

        return res 

    def update(self, index, val):
        """
        Add 'val' to position 'index' in the BIT
        val = +1 means "place an element here"
        val = -1 means "remove element from here"
        """
        # Convert to 1-indexed
        index += 1
        
        # BUG FIX: Should be len(self.bit), not self.n!
        # Original code: while index < self.n: (WRONG!)
        while index < len(self.bit):  # CORRECTED VERSION
            # Add val to current position
            self.bit[index] += val
            # BIT magic: jump to next position that needs updating
            # This ensures all affected nodes in the tree get updated
            index += (index & -index) 

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        """
        Main function to process all queries
        
        Algorithm Overview:
        1. Create virtual position space with front area + original area
        2. For each query:
           - Count elements to the left = current array position
           - Remove element from current virtual position  
           - Add element to next available front position
           - Update tracking and move front pointer left
        """
        
        # Number of queries = number of front positions we'll need
        n = len(queries)
        
        # Create BIT object with our virtual position system
        bit = BIT(m, queries)
        
        # Result array to store answers
        res = []
        
        # ===== INITIALIZATION PHASE =====
        # Place all elements in their original positions
        for i in range(1, m + 1): 
            # Element i goes to virtual position (n + i)
            # This puts elements 1,2,3,4,5 at positions 5,6,7,8,9
            # Leaving positions 1,2,3,4 free for moved elements
            bit.positions[i] = n + i 
            
            # Mark this position as occupied in the BIT
            # update(position, +1) means "add one element at this position"
            bit.update(n + i, 1)

        # ===== QUERY PROCESSING PHASE =====
        for q in queries: 
            # ===== STEP 1: FIND CURRENT POSITION =====
            # Get virtual position where element q currently lives
            current_virtual_pos = bit.positions[q]
            
            # Count how many elements are to the left of this position
            # This gives us the 0-indexed array position!
            # Example: if 2 elements are to the left, then q is at index 2
            array_position = bit.getSum(current_virtual_pos - 1)
            res.append(array_position)
            
            # ===== STEP 2: REMOVE FROM CURRENT POSITION =====
            # Remove element q from its current virtual position
            # update(position, -1) means "remove one element from this position"
            bit.update(bit.positions[q], -1)
            
            # ===== STEP 3: ADD TO FRONT =====
            # Place element q at the current front position (n)
            # update(n, +1) means "add one element at position n"
            bit.update(n, 1)
            
            # ===== STEP 4: UPDATE TRACKING =====
            # Remember that element q is now at front position n
            bit.positions[q] = n
            
            # ===== STEP 5: PREPARE FOR NEXT MOVE =====
            # Decrement n so next moved element goes to position (n-1)
            # This ensures most recently moved elements appear leftmost
            # Sequence: position 4, then 3, then 2, then 1
            n -= 1

        return res

# ===== EXAMPLE WALKTHROUGH =====
# queries = [3,1,2,1], m = 5
#
# Initial setup:
# Virtual positions: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Content:          [-, -, -, -, -, 1, 2, 3, 4, 5]
# BIT values:       [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# n = 4 (next front position)
#
# Query 1: Find element 3
# - Element 3 at virtual position 7
# - Elements to left: getSum(6) = 2 (positions 5,6 occupied)
# - Answer: 2 ✓
# - Move 3 to position 4, n becomes 3
#
# Query 2: Find element 1  
# - Element 1 at virtual position 5
# - Elements to left: getSum(4) = 1 (position 4 occupied by element 3)
# - Answer: 1 ✓
# - Move 1 to position 3, n becomes 2
#
# And so on...