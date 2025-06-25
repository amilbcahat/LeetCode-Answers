"""
RECTANGLE AREA 2 - SWEEP LINE + SEGMENT TREE SOLUTION

PROBLEM: Find total area covered by union of overlapping rectangles

KEY INSIGHT: Break 2D problem into 1D problems
- Sweep Line: Handle Y-dimension (time)
- Segment Tree: Handle X-dimension (space at each Y-level)

VISUAL EXAMPLE:
rectangles = [[0,0,2,1], [1,0,3,1]]

Y=1  ─────────────
     ████████████   ← Both rectangles end here (CLOSE events)
Y=0  ─────────────  
     ████████████   ← Both rectangles start here (OPEN events)
     0   1   2   3
     
Rectangle A: X=[0,2], Y=[0,1] 
Rectangle B: X=[1,3], Y=[0,1]
Union: X=[0,3], Y=[0,1] → Area = 3×1 = 3

ALGORITHM FLOW:
1. Convert rectangles to events: [Y, OPEN/CLOSE, x1, x2]
2. Sort events by Y-coordinate (sweep bottom to top)
3. For each Y-level: calculate area = (width × height)
4. Use segment tree to efficiently calculate X-width (union of intervals)
"""

class SegmentTree:
    """
    Segment Tree for Dynamic Interval Union Queries
    
    PURPOSE: Given a set of X-intervals, efficiently calculate total union length
    EXAMPLE: intervals [0,2], [1,3], [5,6] → union length = (3-0) + (6-5) = 4
    
    KEY INSIGHT: Each node tracks:
    - count: How many intervals cover this EXACT range
    - total: Total union length in this subtree
    
    MAGIC: if count > 0, take full length (automatic union handling!)
    """
    
    def __init__(self, start, end, xArray):
        """
        Initialize segment tree node
        
        start, end: Range of segment indices this node covers
        xArray: Actual X-coordinate values [0,1,2,3,...]
        
        EXAMPLE: SegmentTree(0, 2, [0,1,2,3])
        - Covers segments [0,1], [1,2], [2,3]
        - start=0, end=2 means indices 0,1,2
        """
        self.start = start          # Left boundary (segment index)
        self.end = end              # Right boundary (segment index)
        self.xArray = xArray        # Reference to coordinate array
        self.left = None            # Left child (created lazily)
        self.right = None           # Right child (created lazily)  
        self.count = 0              # How many intervals cover this exact range
        self.total = 0              # Total X-length covered in subtree
    
    def getRangeMid(self):
        """
        Calculate midpoint for binary tree splitting
        
        WHY this formula: Prevents integer overflow
        (start + end) // 2 could overflow, but start + (end-start)//2 cannot
        """
        return self.start + (self.end - self.start) // 2
    
    def getLeft(self):
        """
        Lazy creation of left child
        
        WHY lazy: Memory optimization - only create nodes when needed
        Left child covers [start, mid]
        """
        if self.left is None:
            self.left = SegmentTree(self.start, self.getRangeMid(), self.xArray)
        return self.left
    
    def getRight(self):
        """
        Lazy creation of right child
        
        Right child covers [mid, end]
        
        NOTE: There's intentional overlap at 'mid' in this implementation
        This is a design choice for this specific problem
        """
        if self.right is None:
            self.right = SegmentTree(self.getRangeMid(), self.end, self.xArray)
        return self.right
    
    def update(self, i, j, val):
        """
        Add/remove interval [i,j) with value val (+1 for add, -1 for remove)
        
        VISUAL EXAMPLE: update(1, 3, +1) means "activate segments 1,2"
        
        CASES:
        1. i >= j: Empty range, return 0
        2. Exact match: This node's range = [i,j], update count directly
        3. Partial overlap: Split update between children
        """
        
        # Case 1: Empty range check
        if i >= j:
            return 0  # No coverage for empty range
        
        # Case 2: Perfect match - this node's range exactly matches update range
        if self.start == i and self.end == j:
            self.count += val  # Add/remove interval (+1 for OPEN, -1 for CLOSE)
        else:
            # Case 3: Partial overlap - recurse to children with clipped ranges
            mid = self.getRangeMid()
            
            # Update left child: clip range to [i, min(mid, j)]
            # WHY min(mid, j): Don't exceed left child's boundary
            self.getLeft().update(i, min(mid, j), val)
            
            # Update right child: clip range to [max(mid, i), j] 
            # WHY max(mid, i): Don't go below right child's boundary
            self.getRight().update(max(mid, i), j, val)
        
        # MAGIC TOTAL CALCULATION - The heart of union logic!
        if self.count > 0:
            # If ANY interval covers this range, take FULL length
            # WHY not multiply by count: We want union, not sum!
            # Multiple overlapping intervals still contribute just base length
            self.total = self.xArray[self.end] - self.xArray[self.start]
        else:
            # If no interval covers entire range, sum children's contributions
            # This handles partial coverage automatically
            self.total = self.getLeft().total + self.getRight().total
        
        return self.total  # Return current total union length


class Solution:
    def rectangleArea(self, rectangles):
        """
        SWEEP LINE + SEGMENT TREE ALGORITHM
        
        STEP-BY-STEP PROCESS:
        1. Convert 2D rectangles to 1D events
        2. Sort events by Y-coordinate  
        3. Sweep from bottom to top, calculating area strip by strip
        4. Use segment tree to handle X-interval unions efficiently
        """
        
        # Constants for event types
        OPEN = 1    # Rectangle starts (add X-interval)
        CLOSE = -1  # Rectangle ends (remove X-interval)
        
        # Data structures for coordinate compression and events
        events = []           # List of [Y, OPEN/CLOSE, x1, x2] events
        xCoordinates = set()  # Unique X-coordinates for compression
        
        # STEP 1: Convert rectangles to events and collect X-coordinates
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            
            # Validate rectangle (positive width and height)
            # WHY: Avoid degenerate rectangles that could cause errors
            if x1 < x2 and y1 < y2:
                # Create OPEN event at bottom edge
                # FORMAT: [Y-coordinate, event_type, x_start, x_end]
                events.append([y1, OPEN, x1, x2])
                
                # Create CLOSE event at top edge  
                events.append([y2, CLOSE, x1, x2])
                
                # Collect X-coordinates for compression
                # WHY: Coordinates can be up to 10^9, but we only care about edges
                xCoordinates.add(x1)
                xCoordinates.add(x2)
        
        # STEP 2: Sort events by Y-coordinate (sweep line processing order)
        # WHY: We need to process events from bottom to top
        events.sort()
        
        # STEP 3: Coordinate compression
        # Convert large X-coordinates to small indices for efficiency
        xArray = sorted(xCoordinates)  # [0, 1, 2, 3, ...] 
        xIndexMap = {x: i for i, x in enumerate(xArray)}  # {0:0, 1:1, 2:2, ...}
        
        # STEP 4: Initialize segment tree and algorithm variables
        # Segment tree manages segments between consecutive coordinates
        # If coordinates are [0,1,2,3], segments are [0,1], [1,2], [2,3]
        segmentTree = SegmentTree(0, len(xArray) - 1, xArray)
        
        totalArea = 0       # Accumulate total area
        currentXSum = 0     # Current total X-coverage length
        currentY = events[0][0]  # Current sweep line Y-position
        
        # STEP 5: Process events with sweep line algorithm
        for event in events:
            y, eventType, x1, x2 = event
            
            # CRITICAL: Calculate area BEFORE processing current event
            # WHY: currentXSum represents coverage DURING the strip we just finished
            stripHeight = y - currentY
            stripWidth = currentXSum
            stripArea = stripWidth * stripHeight
            totalArea += stripArea
            
            # VISUAL: Just calculated area of this horizontal strip:
            # ████████████ ← stripWidth = currentXSum
            # ████████████ ← stripHeight = (y - currentY)  
            # ████████████
            
            # Process current event: add/remove X-interval
            x1_index = xIndexMap[x1]  # Convert coordinates to indices
            x2_index = xIndexMap[x2]
            
            # Update segment tree and get new total X-coverage
            currentXSum = segmentTree.update(x1_index, x2_index, eventType)
            
            # Move sweep line to current Y-position
            currentY = y
        
        # STEP 6: Return result with required modulo
        # WHY modulo: Problem requires result mod 10^9+7 to prevent overflow
        return totalArea % (10**9 + 7)