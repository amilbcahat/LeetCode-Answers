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
        def dfs(i, node):
            # Base case: if we've reached the end of the word
            if i == len(word):
                return node.endOfWord  # Return True only if this node is marked as end of a word
                
            if word[i] == ".":  # Handle wildcard character
                # Try all possible paths by checking all children
                for n in node.children:
                    if dfs(i + 1, node.children[n]):  # Recursively check the next character
                        return True  # Return True if any path leads to a match
                return False  # No match found after checking all children
            else:  # Handle regular character
                if word[i] in node.children:  # Check if the character exists in current node's children
                    char = word[i]
                    return dfs(i + 1, node.children[char])  # Continue with the next character
                else:
                    return False  # Character not found, no match possible
                    
        return dfs(0, self.root)  # Start DFS from index 0 and root node

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)