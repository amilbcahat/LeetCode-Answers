class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = { i:[] for i in range(n)}

        #Made an adjacency list 
        for par , child in edges : 
            adj[par].append(child)
            adj[child].append(par)

        #So this DFS is unique , this DFS works on the basis and recursively asking whats the time required to get Apple to each node 
        def dfs(cur , par):
            time = 0 

            #base case is when we reach the leaf node , then dfs , wont happend and we return 0 , meaning , we cant collect apples from them or their children ! 
            for child in adj[cur]:
                if child == par : 
                    #This is used as a technique to avoid using visit set , the only case , where we get an infinite loop is when , we go to the parent back , so we continue that 
                    continue
                #We get the childtime of each node to collect the apple 
                childTime = dfs(child , cur)
                if childTime or hasApple[child]:
                    #If there is childtime , then we now , that subtree of this child has apple 
                    #Otherwise if the child itself has the apple , in that case , childtime is 0 and time would equate to 2 + 0 = 2 , which is actually right as that is the time to do to and fro , from a child which has the apple  
                    time += 2 + childTime 

            return time 

        return dfs(0 , -1)
        