class TrieNode: 
    def __init__(self): 
        self.endOfWord = False
        self.children = {}

class Trie: 
    def __init__(self): 
        self.root = TrieNode()

    def insert(self, word): 
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word): 
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                return False
            cur = cur.children[c]
        return cur.endOfWord 

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for w in dictionary: 
            trie.insert(w)

        memo = {len(s): 0}
        def dfs(i): 
            if i in memo: 
                return memo[i]

            res = dfs(i + 1) + 1 #skip current and add that to results
            curr = trie.root
            for j in range(i, len(s)): 
                char = s[j]
                if char not in curr.children: 
                    break 

                curr = curr.children[char]
                if curr.endOfWord: 
                    res = min(res, dfs(j + 1)) #sub problem


            memo[i] = res
            return res
            
        return dfs(0)