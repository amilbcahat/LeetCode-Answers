class TrieNode: 
    def __init__(self, i): 
        self.children = {}
        self.endOfWord = False

class Trie: 
    def __init__(self):
        self.root = TrieNode(-1)

    def insert(self, word): 
        cur = self.root
        for i, c in enumerate(word): 
            if c not in cur.children: 
                cur.children[c] = TrieNode(i)
            cur = cur.children[c]
        cur.endOfWord = True 

    def search(self, word): 
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix): 
        cur = self.root
        for c in prefix: 
            if c not in cur.children: 
                return False
            cur = cur.children[c]
        return True

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for w in words: 
            trie.insert(w)

        res = []

        for i in range(len(text)): 
            p = trie.root
            for j in range(i, len(text)): 
                ch = text[j]
                if ch not in p.children: 
                    break
                p = p.children[ch]
                if p.endOfWord: 
                    res.append([i , j])

        return res
        



        