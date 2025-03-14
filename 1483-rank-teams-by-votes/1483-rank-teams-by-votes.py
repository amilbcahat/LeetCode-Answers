class Solution:
    def rankTeams(self, votes: List[str]) -> str:

        if len(votes) == 1: 
            return votes[0]

        freqMap = defaultdict(list) #1st, 2nd, 3rd

        for ranking in votes:
            for i in range(len(ranking)):
                if not freqMap[ranking[i]]:
                    freqMap[ranking[i]] = [0] * len(votes[0])
                freqMap[ranking[i]][i] += 1 

        maxHeap = []
        for key in freqMap: 
            ranks = [-val for val in freqMap[key]]
            heapq.heappush(maxHeap, ranks + [key])

        res = ""
        while maxHeap: 
            cur = heapq.heappop(maxHeap) 
            res += cur[-1]

        return res