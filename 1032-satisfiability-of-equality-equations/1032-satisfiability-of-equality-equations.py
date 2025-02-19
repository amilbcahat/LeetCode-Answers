class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # if == , then union them , if found out that != , then check there parents , if equal then means 
        #that they are equal and != condition is false !!
        par = {}
        rank = {}
        
        for eq in equations: 
            par[eq[0]] = eq[0]
            par[eq[3]] = eq[3]
            rank[eq[0]] = 0
            rank[eq[3]] = 0 

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)
            if p1 == p2:
                return False 

            if rank[p1] < rank[p2]: 
                par[p1] = p2 
            elif rank[p2] < rank[p1]: 
                par[p2] = p1
            else:
                par[p1] = p2
                rank[p2] += 1
            return True 

        for eq in equations:
            if eq[1] == "=" and eq[2] == "=": 
                ch1 = eq[0]
                ch2 = eq[3]
                union(ch1, ch2)

        for eq in equations:
            if eq[1] != "=" or eq[2] != "=": 
                ch1 = eq[0]
                ch2 = eq[3]
                p1 = find(ch1)
                p2 = find(ch2)
                print(p1, p2)
                if p1 == p2: 
                    return False
        print(par)
        return True 