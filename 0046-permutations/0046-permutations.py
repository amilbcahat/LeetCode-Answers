class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #Neetcode Video 
        perms = [[]]
        #[[1]]
        #[[1 , 2] , [2 , 1]] Add 2 , to every index of both 
        # Now add 3 at every index of both 
        for n in nums : 
            new_perms = []
            for p in perms : 
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i , n)
                    new_perms.append(p_copy)
            perms = new_perms 
        return perms 