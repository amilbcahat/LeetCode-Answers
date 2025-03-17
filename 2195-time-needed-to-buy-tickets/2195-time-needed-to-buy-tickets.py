class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while tickets[k] != 0: 
            for t in range(len(tickets)): 
                if tickets[t] > 0: 
                    time += 1
                    tickets[t] -= 1
                    if t == k and tickets[t] == 0: 
                        return time 

        

