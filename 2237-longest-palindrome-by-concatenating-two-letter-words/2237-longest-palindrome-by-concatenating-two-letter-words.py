class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        s = spare = 0 
        store = Counter(words)
        for w in store: 
            if w[0] != w[1]:
                s += min(store[w], store[w[::-1]]) * 2 

            else: 
                if store[w] > 1: 
                    s += (store[w] // 2) * 4
                if store[w] % 2: 
                    spare = 2

        return s + spare
                