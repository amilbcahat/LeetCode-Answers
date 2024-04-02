class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Simple mapping 
        mp = defaultdict(str)
        alreadyMapped = set()
        for i in range(len(s)) : 
            if s[i] not in mp : 
                mp[s[i]] = t[i]
            else : 
                if mp[s[i]] != t[i] :
                    # return False   
                    return False 

        #If a t value has been already mapped , then return False 
        return len(mp.keys()) == len(set(mp.values()))
