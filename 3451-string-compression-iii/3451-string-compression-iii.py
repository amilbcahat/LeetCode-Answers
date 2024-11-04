class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""

        def dfs(prevChar ,timeOccured, i):
            nonlocal comp
            if i == len(word): 
                comp += (str(timeOccured + 1) + prevChar)
                return comp

            if prevChar == word[i]: 
                timeOccured += 1
        
            # print(prevChar ,timeOccured, i)
            if timeOccured == 9: 
                comp += ("9" + word[i])
                dfs(word[i], 0, i + 1)
            elif timeOccured < 9 and prevChar != word[i]: 
                comp += (str(timeOccured + 1) + prevChar)
                dfs(word[i], 0, i + 1)
            else: 
                dfs(word[i], timeOccured, i + 1)

        dfs(word[0], 0 , 1)
        return comp

            

             
