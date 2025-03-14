class Rank: 
    def __init__(self, cnt, key): 
        self.cnt = cnt
        self.key = key

    def __lt__(self, other): 
        if self.cnt != other.cnt: 
            return self.cnt > other.cnt #normally should return if < , but value is going in maxHeap heap, thhats why its opposite 
        else: 
            return self.key < other.key

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1: 
            return votes[0]

        num_teams = len(votes[0])
        freqMap = defaultdict(lambda: [0] * num_teams) #1st, 2nd, 3rd

        for ranking in votes:
            for i in range(len(ranking)):
                letter = ranking[i]       
                freqMap[letter][i] += 1 

        maxHeap = []
        for key, val in freqMap.items():        
            heapq.heappush(maxHeap, Rank(val, key))

        res = ""
        while maxHeap: 
            res += heapq.heappop(maxHeap).key 

        return res