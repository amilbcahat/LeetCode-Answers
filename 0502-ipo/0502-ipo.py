class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(c , p) for c , p in zip(capital, profits)] 
        heapq.heapify(projects)

        print(sorted(projects))
        maxHeap = [] #to get for max minimum capital , most profitable

        cur_capital = w
        affordable_projects = [] #Most profitable among available project (under specified capital)
        while (projects or affordable_projects) and k: 
            while projects and projects[0][0] <= cur_capital :
                cap, profitEarned = heapq.heappop(projects)
                heapq.heappush(affordable_projects, (-profitEarned, cap))

            if affordable_projects: 
                #Most Profitable and Affordable
                profitEarned, cap = heapq.heappop(affordable_projects)
                cur_capital += -profitEarned

            k -= 1
        return cur_capital
        