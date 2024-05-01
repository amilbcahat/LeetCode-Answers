class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1 
        for i in range(len(word)) : 
            if word[i] == ch : 
                idx = i 
                break

        if idx == -1 : 
            return word 
        else : 
            res = ""

            for i in range(idx , -1 , -1):
                res += word[i]

            return res + word[idx + 1 : ]