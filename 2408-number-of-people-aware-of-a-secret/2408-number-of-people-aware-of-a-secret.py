class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        #With Two deques - Check Editorial
        know, share = deque([(1, 1)]), deque()
        know_cnt, share_cnt = 1, 0 

        for i in range(2, n + 1): 
            #Two different queues, handling two different cases
            if know and know[0][0] == i - delay: 
                know_cnt -= know[0][1]
                share_cnt += know[0][1]
                share.append(know[0])
                know.popleft()
            if share and share[0][0] == i - forget: 
                share_cnt -= share[0][1]
                share.popleft()
            if share: 
                know_cnt += share_cnt
                know.append((i, share_cnt))

        return (know_cnt + share_cnt) % (10 ** 9 + 7)
        # With queue
        # queue = deque() #start, end  
        # t = 0
        # queue.append((t + delay, t + forget)) 
        # t += 1
        # sharedwith = 1  
        # while queue and t < n:
        #     #Remove people who cant share anymore
        #     # while queue[0][1] == t: 
        #     #     queue.popleft()
        #     #     sharedwith -= 1

        #     for peopleStart, peopleEnd in queue.copy(): 
        #         #For people that are in queue
        #         #They can share to new individuals
        #         #Also add these new individuals to whom the secrets was shared to queue
        #         #People can only share the secret, when their own delay to share is over
        #         if peopleStart <= t < peopleEnd: 
        #             queue.append((t + delay, t + forget))
        #             sharedwith += 1

        #     print(queue, t, sharedwith)
        #     t += 1 


        # return sharedwith
