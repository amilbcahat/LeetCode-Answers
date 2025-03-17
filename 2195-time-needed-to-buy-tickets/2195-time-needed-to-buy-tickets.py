class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # time = 0
        # some = tickets 
        # while tickets[k] != 0: 
        #     for t in range(len(tickets)): 
        #         if tickets[t] > 0: 
        #             time += 1
        #             tickets[t] -= 1
        #             print(time, tickets)
        #             if t == k and tickets[t] == 0: 
        #                 print("boom")
        #                 # return time 

        required = tickets[k]
        time = 0
        for i in range(len(tickets)): 
            if i <= k: 
                time += required if tickets[i] > required else tickets[i]
            else: 
                time += required - 1 if tickets[i] >= required else tickets[i]

        return time 
        



        

