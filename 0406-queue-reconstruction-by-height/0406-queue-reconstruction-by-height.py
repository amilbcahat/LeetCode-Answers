class SegmentTree: 
    def __init__(self, people): 
        n = len(people)
        self.people = people 
        # Standard segment tree size is 4*n to handle all possible nodes
        self.tree = [0] * (4 * n)
        self.result = [None] * n 

    def buildTree(self, index, start, end):
        # VACANT SPOT CONCEPT: Each position initially has 1 vacant spot (empty)
        if start == end: 
            self.tree[index] = 1  # Leaf node = 1 vacant spot at this position
            return 

        # Using 0-based indexing: left child = 2*i+1, right child = 2*i+2
        mid = (start + end) // 2
        self.buildTree(2 * index + 1, start, mid)      # Left child
        self.buildTree(2 * index + 2, mid + 1, end)    # Right child
        
        # Internal nodes store SUM of vacant spots in their range
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def query(self, index, left, right, position, height, originalPos): 
        """
        position = (k+1)th vacant spot we're looking for
        - For person [height, k], we need k people in front
        - So we need the (k+1)th vacant spot from left
        """
        
        # Base case: Found the exact position (leaf node)
        if left == right: 
            self.result[left] = [height, originalPos]  # Place person here
            self.tree[index] -= 1  # Mark this position as occupied (1 -> 0)
            return  # CRITICAL: Must return to stop execution after placement
        
        # Pruning: This subtree can't accommodate our request
        if self.tree[index] < position: 
            return  # Not enough vacant spots in this subtree, abandon this path

        mid = (left + right) // 2
        
        # DECISION LOGIC: Which subtree contains our target vacant spot?
        # Check if LEFT child has enough vacant spots for our position
        if self.tree[2 * index + 1] >= position: 
            # Left subtree can handle it, go left with same position
            self.query(2 * index + 1, left, mid, position, height, originalPos)
        else:
            # Left subtree doesn't have enough, must go RIGHT
            # POSITION ADJUSTMENT: If left has 2 vacant spots and we want 4th,
            # then in right subtree we want the (4-2) = 2nd vacant spot
            self.query(2 * index + 2, mid + 1, right, 
                      position - self.tree[2 * index + 1], height, originalPos)

        # PATH UPDATE: Update every node on the path from root to leaf
        # This maintains accurate vacant counts for future queries
        # Both leaf AND internal nodes need updating for tree consistency
        self.tree[index] -= 1


class Solution:
    def reconstructQueue(self, people):
        """
        SORTING STRATEGY: Process people to satisfy constraints correctly
        1. Sort by height (ascending): shorter people first
        2. Sort by k (descending) for same heights: higher k first among equals
        
        WHY THIS ORDER?
        - Shorter first: When we place someone, all previously placed are shorter/equal
        - Higher k first: Among same heights, handle "pickier" people first
        """
        people.sort(key=lambda x: (x[0], -x[1]))  # -x[1] makes k descending
        
        n = len(people)
        seg = SegmentTree(people)
        seg.buildTree(0, 0, n - 1)  # Initialize all positions as vacant
        
        # PLACEMENT LOOP: Place each person in their correct position
        for p in people: 
            # p[1] = k value, p[1] + 1 = (k+1)th vacant spot needed
            # CONSTRAINT TRANSLATION: k people in front -> (k+1)th vacant spot
            seg.query(0, 0, n - 1, p[1] + 1, p[0], p[1])

        return seg.result