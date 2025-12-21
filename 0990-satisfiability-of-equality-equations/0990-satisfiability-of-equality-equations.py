class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par = {}
        rank = {}

        for eq in equations: 
            par[eq[0]] = eq[0]
            par[eq[3]] = eq[3]
            rank[eq[0]] = 0 
            rank[eq[3]] = 0


        def find(p):
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]

            return p


        def union(n1, n2):
            p1 , p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                par[p1] = p2 
            elif rank[p1] > rank[p2]:
                par[p2] = p1 
            else:
                par[p1] = p2 
                rank[p2] += 1


        for eq in equations:
            if eq[1] == "=" and eq[2] == "=":
                union(eq[0], eq[3])

        for eq in equations: 
            if eq[1] != "=" or eq[2] != "=":
                p1 = find(eq[0])
                p2 = find(eq[3])
                if p1 == p2: 
                    return False 

        return True 