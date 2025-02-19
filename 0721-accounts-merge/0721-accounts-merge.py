class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        edges = []
        nodes = set()
        nameToAcc = defaultdict(str)

        for account in accounts: 
            name = account[0]
            for email in account[1:]:
                nameToAcc[email] = name 
        n = list(nameToAcc.keys())
        #Each email is a node 
        #We will use union find algo for this 
        par = {}
        rank = {}

        for email in nameToAcc:
            par[email] = email
            rank[email] = 0 

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
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

        edges = []
        for acc in accounts:
            for i in range(1, len(acc) - 1): 
                union(acc[i], acc[i + 1])

        # print(par)
        trackPar = defaultdict(list)
        for child in par: 
            #Find parent
            parent = find(child)
            trackPar[parent].append(child)

        res = []
        for par in trackPar: 
            cur = []
            #name 
            name = nameToAcc[par]
            cur.append(name)
            for child in sorted(trackPar[par]): 
                cur.append(child)
            res.append(cur)

        # print(res)
        return sorted(res)
        

                