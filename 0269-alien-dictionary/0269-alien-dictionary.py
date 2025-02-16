class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set) #words
        nodes = set(char for word in words for char in word)

        for i in range(len(words) - 1): 
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2: 
                return ""

            for j in range(min(len(w1), len(w2))): 
                if w1[j] != w2[j]: 
                    adj[w1[j]].add(w2[j])
                    break

        print(nodes)

        visited, path = set(), []
        topSort = []
        def dfs(src): 
            if src in path: 
                return False

            if src in visited: 
                return True

            path.append(src)
            for nei in adj[src]: 
                if not dfs(nei):
                    return False

            path.remove(src)
            visited.add(src)
            topSort.append(src)

            return True
        
        for n in nodes: 
            if not dfs(n):
                return ""

        return "".join(topSort[::-1])  

#         Let me explain why only the first different character matters in lexicographical ordering by using a familiar example - English dictionary:

# ```
# Consider two words:
# "cat" vs "car"

# In English dictionary order:
# 1. First, compare 'c' = 'c' (same, move on)
# 2. Then compare 'a' = 'a' (same, move on)
# 3. Finally compare 't' vs 'r'
#    Since 'r' comes before 't' in English,
#    "car" comes before "cat"
# ```

# Key Point: Once we find 't' comes after 'r', that's ALL we learn about the alphabet order.

# Why?
# ```
# "cat" vs "car"
# - We learn 'r' comes before 't'
# - The position of any characters after this doesn't matter
# - Because just like English, words are sorted by their first point of difference
# ```

# Real Example from problem:
# ```
# "wrt" vs "wrf"
# w = w (same)
# r = r (same)
# t ≠ f (FIRST DIFFERENCE!)
# - We learn 't' comes before 'f'
# - This is the ONLY valid information about letter ordering
# - Any characters after this wouldn't give us valid information about the alien alphabet
# ```

# If we didn't break:
# ```
# word1 = "abc"
# word2 = "abd"

# Without break:
# - Learn 'c' comes before 'd' (WRONG!)
# - The words are ordered this way because of first difference
# - Later characters don't imply any ordering
# ```              