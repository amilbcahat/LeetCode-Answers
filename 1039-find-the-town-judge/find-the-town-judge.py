class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #Use Graph Concept 

        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for fro , to in trust : 
            indegree[to] += 1 
            outdegree[fro] += 1 
            

        for fro , to in trust : 
            if outdegree[to] == 0 and indegree[to] == n - 1 : 
                return to
        return n if not trust and n == 1 else -1 