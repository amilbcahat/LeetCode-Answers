class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p , s] for p , s in zip(position , speed)]

        stack = [] 
         
        for p , s in sorted(pairs)[::-1]:
            stack.append((target - p) / s) 
            #length must be more or equal to 2 , because we need a condition for collision
            if len(stack) >= 2 and stack[-1] <= stack[-2] : 
                #cur carries has more speed that last so they collide and become a fleet 
                #cur car starts moving with the car infront !
                stack.pop()
        return len(stack)