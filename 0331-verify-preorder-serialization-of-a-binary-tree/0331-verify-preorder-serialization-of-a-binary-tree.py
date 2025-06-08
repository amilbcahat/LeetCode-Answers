class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        available_slots = 1 

        for i in range(len(preorder)): 
            if preorder[i] == ',': 
                available_slots -= 1

                if available_slots < 0: 
                    return False

                if preorder[i - 1] != "#": 
                    available_slots += 2 

        available_slots = available_slots - 1 if preorder[-1] == "#" else available_slots + 2

        return available_slots == 0