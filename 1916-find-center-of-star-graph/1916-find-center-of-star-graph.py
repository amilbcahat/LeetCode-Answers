class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        m = defaultdict(int)
        
        for src , dst in edges : 
            m[src] += 1 
            m[dst] += 1 

        print(m)
        for n in m : 
            if m[n] == len(edges):
                return n