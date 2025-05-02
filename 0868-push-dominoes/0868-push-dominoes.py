class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #Force Calculation 
        N = len(dominoes)
        force = [0] * N 
        f = 0 
        for i in range(N): 
            if dominoes[i] == "R": 
                f = N 
            elif dominoes[i] == "L": 
                f = 0 
            else:
                f = max(f - 1, 0)
            force[i] += f 

        for i in range(N - 1, -1 , -1): 
            if dominoes[i] == "R": 
                f = 0
            elif dominoes[i] == "L": 
                f = N
            else:
                f = max(f - 1, 0)

            force[i] -= f 

        return "".join("." if f == 0 else "R" if f > 0 else "L" for f in force)

        # Simulate and build cases 
        # dominoes = list(dominoes)
        # last = ['', 0]
        # for i, c in enumerate(dominoes):
        #     if c == 'L': 
        #         if last[0] == 'R': 
        #             l = last[1]
        #             r = i 
        #             while l < r: 
        #                 dominoes[l] = 'R'
        #                 dominoes[r] = 'L'
        #                 l += 1 
        #                 r -= 1

        #         else: 
        #             for j in range(last[1], i + 1): 
        #                 dominoes[j] = 'L'
        #         last = ['L', i]
        #     elif c == 'R': 
        #         if last[0] == 'R': 
        #             for j in range(last[1], i + 1): 
        #                 dominoes[j] = 'R'
        #         else:
        #             pass

        #         last = ['R', i]

        # if last[0] == 'R': 
        #     for i in range(last[1], len(dominoes)): 
        #         dominoes[i] = 'R'

        # return "".join(dominoes)
            