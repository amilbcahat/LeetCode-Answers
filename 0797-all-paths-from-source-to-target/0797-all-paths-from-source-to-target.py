class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Editorial please check always
        # This will help in understanding that - https://math.stackexchange.com/a/3961816
        # Backtracking
        # n = len(graph)
        # res = []
        # def dfs(node, path):
        #     nonlocal res 
        #     if node == n - 1: 
        #         res.append(list(path))
        #         return

        #     for nei in graph[node]: 
        #         path.append(nei)
        #         dfs(nei, path) 
        #         path.pop()

        # dfs(0, [0])

        # return res

        #Top Down Approach 
        # allPathsToTarget(currNode)={currNode+allPathsToTarget(nextNode)}
        target = len(graph) - 1

        @lru_cache(maxsize=None)
        def all_paths_to_target(node): 
            if node == target: 
                return [[target]]

            path_to_target_from_this_node = []
            for nei in graph[node]: 
                for path in all_paths_to_target(nei): 
                    path_to_target_from_this_node.append([node] + path)
            
            return path_to_target_from_this_node

        return all_paths_to_target(0)

#         The Key Insight: How Many Paths Can Exist?
# First, let's understand why we get 2^N paths in the worst case:
# Imagine a graph where every node can reach every node that comes after it:

# Node 0 → can go to nodes 1, 2, 3, ..., N-1
# Node 1 → can go to nodes 2, 3, ..., N-1
# Node 2 → can go to nodes 3, ..., N-1
# And so on...

# For each intermediate node (nodes 1 to N-2), we have a choice: include it in our path or skip it. Since we have N-2 intermediate nodes, and each gives us 2 choices, we get 2^(N-2) possible paths, which simplifies to 2^N paths in big-O notation.
# Time Complexity Breakdown
# Approach 1: Backtracking - O(2^N × N)
# What happens:

# We explore 2^N possible paths (in worst case)
# For each path we find, we need to copy it to our result
# Each path can have up to N nodes, so copying takes O(N) time

# Simple math:

# Number of paths: 2^N
# Time to process each path: N
# Total time: 2^N × N

# Think of it like this: You're exploring a maze with 2^N possible routes, and each time you find a complete route, you need to write down all N steps of that route.
# Approach 2: Dynamic Programming - O(2^N × N)
# What happens:

# We still find the same 2^N paths
# But now we're copying intermediate results multiple times as we build up solutions
# We copy paths at every level of recursion, not just at the end

# Why it's the same complexity but slower in practice:

# Same number of total operations: 2^N × N
# But more copying overhead because we copy partial paths during computation
# Backtracking only copies complete paths at the end

# Easy Memory Trick
# Both approaches have the same worst-case time complexity, but:

# Backtracking = More efficient in practice (less copying)
# Dynamic Programming = Same theoretical complexity but more overhead

# Visual Example
# For a 4-node graph (0→1→2→3), possible paths might be:

# 0→3 (direct)
# 0→1→3
# 0→2→3
# 0→1→2→3

# That's 4 paths, and each path has at most 4 nodes, so we do roughly 4×4 = 16 operations total.
# The 2^N factor comes from the exponential growth of possible paths as the graph gets bigger!
# Does this help clarify the time complexity? The key insight is that both algorithms do the same amount of work fundamentally - they just organize it differently







        
# 6