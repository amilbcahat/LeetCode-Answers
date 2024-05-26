class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        # cur = []
        # res = []

        # def backtrack(i):
        #     if i == len(s):
        #         print(cur)
        #         res.append(" ".join(cur))
        #         return 

        #     for j in range(i , len(s)):
        #         w = s[i : j + 1]
        #         if w in wordDict : 
        #             cur.append(w)
        #             backtrack(j + 1)
        #             cur.pop()

        # backtrack(0)
        # return res 

        #Optimal Subproblem solution !
        cache = {}
        def backtrack(i):
            if i == len(s):
                #Was able to make a string 
                return [""]

            if i in cache:
                return cache[i]
            #Could not make any string 
            res = []
            for j in range(i, len(s)):
                #xxxxx -> xxxx , xxx , xx , x are the subproblem 
                w = s[i : j + 1]
                  #does not matter in this case 
                if w not in wordDict: 
                    continue
                
                #Gets some strings in array 
                strings = backtrack(j + 1)
                #Add space as required 
                for substr in strings : 
                    sentence = w 
                    if substr : 
                        sentence += " " + substr
                    #if no substr then append this string 
                    res.append(sentence)
            cache[i] = res 
            return res 

        return backtrack(0)