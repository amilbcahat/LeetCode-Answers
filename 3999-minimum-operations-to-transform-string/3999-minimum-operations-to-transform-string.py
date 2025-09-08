class Solution:
    def minOperations(self, s: str) -> int:
        largest = -1 
        for c in s: 
            largest = max(ord('z') - ord(c) + 1 if c != 'a' else 0, largest)

        return largest