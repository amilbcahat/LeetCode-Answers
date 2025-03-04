class TrieNode: 
    def __init__(self): 
        self.endOfWord = False 
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True 

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word): 
                return node.endOfWord

            if word[i] == ".": 
                #Look at the next node in trie (change one level up)
                for n in node.children: 
                    if dfs(i + 1, node.children[n]):
                        return True
                return False
            else: 
                if word[i] in node.children: 
                    char = word[i]
                    return dfs(i + 1, node.children[char])
                else: 
                    return False
        
        
        return dfs(0, self.root)

        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)