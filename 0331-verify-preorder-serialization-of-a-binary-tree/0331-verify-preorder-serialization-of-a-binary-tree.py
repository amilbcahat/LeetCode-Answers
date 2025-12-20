class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1 
        preorder = preorder.split(',')

        for node in preorder: 
            slots -= 1
            if slots < 0: 
                return False 
            if node != '#':
                slots += 2
            


        return slots == 0