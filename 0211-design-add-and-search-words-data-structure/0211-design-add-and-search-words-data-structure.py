class TrieNode:
    def __init__(self):
        self.endOfWord = False  # Flag to mark if this node represents the end of a word
        self.children = {}      # Dictionary to store child nodes, with characters as keys
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # Initialize with an empty root node
        
    def addWord(self, word: str) -> None:
        cur = self.root         # Start from the root
        for c in word:          # Process each character in the word
            if c not in cur.children:
                cur.children[c] = TrieNode()  # Create a new node if the character doesn't exist
            cur = cur.children[c]             # Move to the next node
        cur.endOfWord = True    # Mark the last node as the end of a word
        
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)): 
                c = word[i]
                if c == ".": 
                    for child in cur.children.values(): 
                        if dfs(i + 1, child): 
                            return True 
                    return False
                else: 
                    if c not in cur.children: 
                        return False 
                    cur = cur.children[c]
            
            return cur.endOfWord
        
        return dfs(0, self.root)
                    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)