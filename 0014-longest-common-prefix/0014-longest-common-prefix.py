class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            #Map index to each string in strs 
            for s in strs : 
                if i == len(s) or s[i] != strs[0][i]:
                    #Return when invalid
                    return res 
            res += strs[0][i]

        #Return when done 

        return res 
