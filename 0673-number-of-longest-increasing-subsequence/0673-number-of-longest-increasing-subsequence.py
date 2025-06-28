"""
\U0001f3af PROBLEM: Find Number of Longest Increasing Subsequences (LIS)

\U0001f9e0 MEMORY AID - "The Restaurant Reservation System":
Think of BIT as a restaurant reservation system where:
- Each table (index) tracks: max_party_size_served, how_many_parties_of_that_size
- We process customers (array elements) in height order (shortest first)
- For each customer, we check: "What's the biggest party served at tables before mine?"
- Then we make a new reservation: "previous_max + 1 people, extending all those parties"

\U0001f4da KEY CONCEPTS TO REMEMBER:
1. SORTING: Process by value (shortest first), break ties by index (latest first)
2. BIT STRUCTURE: Each node stores (maxLength, frequency) - not just one value!
3. THREE OPERATIONS: getMax, getFrequency, update - each with specific BIT traversal
4. QUERY LOGIC: "What can I extend?" then "How many ways can I extend it?"
"""

class BIT: 
    def __init__(self):
        # \U0001f3af REMEMBER: BIT nodes store TWO pieces of info
        self.maxLength = 0   # Longest LIS ending at positions ≤ this index
        self.frequency = 0   # How many such longest LIS exist

class Solution:
    
    def getMax(self, index): 
        """
        \U0001f50d QUERY: "What's the longest LIS ending at any position ≤ index?"
        
        \U0001f9e0 MEMORY: Think "climbing up the family tree to find the tallest ancestor"
        - Start at leaf (index)
        - Keep going to parents: index -= index & -index
        - Track maximum height seen
        """
        index += 1  # \U0001f6a8 REMEMBER: Convert to 1-indexed for BIT
        maxRes = 0
        while index > 0:
            maxRes = max(maxRes, self.bit[index].maxLength)
            index -= index & -index  # \U0001f3af BIT parent traversal
        return maxRes

    def getFrequency(self, index, maxLength): 
        """
        \U0001f522 QUERY: "How many LIS of exactly 'maxLength' end at positions ≤ index?"
        
        \U0001f9e0 MEMORY: Think "counting specific-sized parties at tables ≤ index"
        - Same traversal as getMax
        - But only count nodes where maxLength matches exactly
        """
        index += 1  # \U0001f6a8 REMEMBER: Convert to 1-indexed
        res = 0
        while index > 0:
            if self.bit[index].maxLength == maxLength:
                res += self.bit[index].frequency
            index -= index & -index  # \U0001f3af Same parent traversal
        return res

    def update(self, index, maxLength, frequency): 
        """
        \U0001f4dd UPDATE: "Record new LIS info and propagate to affected nodes"
        
        \U0001f9e0 MEMORY: Think "updating reservation system from bottom to top"
        - Start at position
        - Update all nodes that should know about this position
        - Go to children: index += index & -index
        
        \U0001f6a8 CRITICAL INDENTATION: index += index & -index MUST be INSIDE while loop!
        """
        index += 1  # \U0001f6a8 REMEMBER: Convert to 1-indexed
        while index <= self.n:
            if self.bit[index].maxLength < maxLength:
                # New record! Replace old info
                self.bit[index].maxLength = maxLength
                self.bit[index].frequency = frequency
            elif self.bit[index].maxLength == maxLength:
                # Same length, add to frequency count
                self.bit[index].frequency += frequency
            index += index & -index  # \U0001f3af BIT children traversal - INSIDE LOOP!

    def findNumberOfLIS(self, nums) -> int:
        """
        \U0001f3af MAIN ALGORITHM: Process elements to build LIS information
        
        \U0001f9e0 MEMORY SEQUENCE:
        1. SORT: "Serve customers by height, taller ones can extend shorter ones' parties"
        2. PROCESS: For each customer: "What can I extend?" → "Extend it!"
        3. FINAL: "What's the biggest party size overall?" → "How many such parties?"
        """
        
        self.n = len(nums)
        # \U0001f6a8 REMEMBER: Use list comprehension for separate objects!
        self.bit = [BIT() for _ in range(self.n + 1)]
        
        indices = list(range(self.n))
        
        # \U0001f3af SORTING STRATEGY: "Shorter first, among equals process later indices first"
        # WHY: When processing an element, all previous elements have ≤ value
        # This ensures we can always extend previous subsequences
        indices.sort(key=lambda x: (nums[x], -x))

        for index in indices: 
            # \U0001f50d STEP 1: "What's the longest LIS ending before my position?"
            curMax = self.getMax(index)

            if curMax == 0: 
                # \U0001f195 BASE CASE: "No LIS before me, start fresh"
                self.update(index, 1, 1)  # Length 1, frequency 1
                continue

            # \U0001f522 STEP 2: "How many LIS of that max length can I extend?"
            # \U0001f6a8 CRITICAL: Ask for curMax, NOT curMax + 1!
            freq = self.getFrequency(index, curMax)
            
            # \U0001f4dd STEP 3: "Create new LIS by extending those found"
            self.update(index, curMax + 1, freq)  # New length, same frequency

        # \U0001f3c1 FINAL ANSWER: "What's the overall max?" → "How many of that max?"
        maxLength = self.getMax(self.n - 1)  # Overall maximum LIS length
        return self.getFrequency(self.n - 1, maxLength)  # Count of max LIS


"""
\U0001f3af REVISION CHECKLIST - Common Mistakes to Avoid:

❌ WRONG: self.bit = [BIT()] * (n+1)          ✅ RIGHT: [BIT() for _ in range(n+1)]
❌ WRONG: freq = getFrequency(index, curMax+1) ✅ RIGHT: getFrequency(index, curMax)  
❌ WRONG: while loop: \n    process \n index += ...  ✅ RIGHT: while loop: \n    process \n    index += ...
❌ WRONG: max(maxRes, maxRes, bit[i].maxLength) ✅ RIGHT: max(maxRes, bit[i].maxLength)
❌ WRONG: return maxRes (in getFrequency)     ✅ RIGHT: return res

\U0001f9e0 MEMORY AIDS:
- BIT = "Binary Indexed Tree" = "Restaurant Reservation System"
- Sort = "Serve shortest customers first so they can extend each other's parties"  
- getMax = "What's the tallest ancestor in family tree?"
- getFrequency = "Count parties of exact size at tables ≤ index"
- update = "Update reservation system from leaf to root"
- Main logic = "What can extend? → How many ways? → Extend them all!"
"""
