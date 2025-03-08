class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}
        self.topWords = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root 
        for c in word :
            if c not in cur.children: 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            if len(cur.topWords) < 3:
                cur.topWords.append(word)
        cur.endOfWord = True 

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return [] 
            cur = cur.children[c]
        return cur.topWords
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
        return cur.endOfWord 


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for w in products:
            trie.insert(w)

        res = []
        prefix = ""
        for c in searchWord:
            prefix += c
            res.append(trie.startsWith(prefix))

        return res