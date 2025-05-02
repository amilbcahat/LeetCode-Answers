from collections import deque
from collections import defaultdict

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #Overkill BFS on 1D Array - process dominoes level by level
        dominoes = list(dominoes)  # Convert to list for in-place modifications
        
        queue = deque()  # Queue to track positions of falling dominoes
        
        # Initialize queue with dominoes that are already falling
        for i in range(len(dominoes)): 
            if dominoes[i] == 'L' or dominoes[i] == 'R': 
                queue.append((i, dominoes[i]))
        
        # Process dominoes level by level (simulating time steps)
        while queue: 
            size = len(queue)  # Number of dominoes to process at current level
            collection = defaultdict(list)  # Track affected positions and their forces
            
            # Process all dominoes at current level before moving to next level
            for _ in range(size): 
                pos, d = queue.popleft()  # Get next domino position and direction
                next_pos = pos - 1 if d == 'L' else pos + 1  # Calculate next affected position
                
                # Check if next position is valid for left-falling domino
                if d == 'L' and next_pos >= 0 and dominoes[next_pos] == ".": 
                    collection[next_pos].append("L")
                # Check if next position is valid for right-falling domino
                elif d == 'R' and next_pos < len(dominoes) and dominoes[next_pos] == ".": 
                    collection[next_pos].append("R")
            
            # Resolve collisions and update queue for next level
            for pos in collection: 
                # If two forces hit same position, they cancel out (collision)
                if len(collection[pos]) == 2: 
                    dominoes[pos] = "."  # Fixed: was == instead of = (this was a bug)
                else: 
                    # Otherwise, domino falls in the direction of the force
                    dominoes[pos] = collection[pos][0]
                    # Add to queue for next level processing
                    queue.append((pos, collection[pos][0]))
        
        return ''.join(dominoes)  # Convert back to string and return


        #Force Calculation 
        # N = len(dominoes)
        # force = [0] * N 
        # f = 0 
        # for i in range(N): 
        #     if dominoes[i] == "R": 
        #         f = N 
        #     elif dominoes[i] == "L": 
        #         f = 0 
        #     else:
        #         f = max(f - 1, 0)
        #     force[i] += f 

        # for i in range(N - 1, -1 , -1): 
        #     if dominoes[i] == "R": 
        #         f = 0
        #     elif dominoes[i] == "L": 
        #         f = N
        #     else:
        #         f = max(f - 1, 0)

        #     force[i] -= f 

        # return "".join("." if f == 0 else "R" if f > 0 else "L" for f in force)

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
            