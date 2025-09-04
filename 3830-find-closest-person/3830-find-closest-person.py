class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z - x) == abs(z - y):
            return 0
            
        return 1 if abs(z - x) < abs(z - y) else 2