class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        visit = set()
        def dfs(i):
            if i == len(nums):
                return [[]]


            resPerms = []
            perms = dfs(i + 1)
            #
            for p in perms : 
                for j in range(len(p) + 1):
                    # Skip duplicate insertions at the same position (exp - 1)
                    if j > 0 and nums[i] == p[j - 1]:
                        continue 
                    pCopy = p.copy()
                    pCopy.insert(j , nums[i])
                    t = tuple(pCopy)
                    #Create a unique identifier t for this permutation to avoid duplicates (Exp - 2)
                    if t not in visit :
                        visit.add(t)
                        resPerms.append(pCopy)
    
            return resPerms 

        return dfs(0)
        #Returns unique lists 
        # return [list(i) for i in set(tuple(i) for i in dfs(0))]


        
#Exp - 1

# The line if j > 0 and nums[i] == p[j - 1]: continue in the context of generating unique permutations is a crucial optimization that helps to avoid generating duplicate permutations when the input list contains repeated elements.
# Here's a breakdown of what this line does and why it's important:

# j > 0: This condition checks if the current position j in the permutation p is not the first position. This is necessary because if j is 0, then p[j - 1] would be out of bounds.

# nums[i] == p[j - 1]: This condition checks if the current element nums[i] that we are trying to insert into the permutation p is the same as the element just before the current position j in p (p[j - 1]).

# continue: If both conditions are met, this command skips the current iteration of the loop and moves to the next iteration. Essentially, it means "do not insert nums[i] into position j of permutation p if it's the same as the element in position j-1, and only proceed if we're not at the first position."

# Why is this important?

# This optimization is crucial for avoiding duplicates in the context of permutations with repeated elements. Consider an example where you have a partial permutation [... , 2] and you're about to insert another 2 into it. If you insert the second 2 right after the first, you'd get [... , 2, 2], which is fine. However, if you try to insert the second 2 into any other position, you'd essentially be creating a permutation that is equivalent to one that you'd already have counted, thus creating a duplicate.

# By employing this check, you ensure that you only add an element nums[i] into the permutation p if it does not immediately follow an identical element (nums[i] == p[j - 1]). This effectively skips unnecessary iterations that would lead to duplicate permutations, thereby ensuring the uniqueness of each permutation in the final result.

#Exp - 2 
#The use of if identifier not in visit: followed by visit.add(identifier) serves a slightly different purpose. It's a broader check that can prevent the algorithm from considering the same permutation again, regardless of the insertion position. This can be particularly useful if there are other ways duplicates might arise in your algorithm outside of the immediate insertion logic.
#