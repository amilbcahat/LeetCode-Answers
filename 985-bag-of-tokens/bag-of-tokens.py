class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        print(tokens)
        l ,r = 0 ,len(tokens) - 1
        score = 0 
        maxScore = 0
        #Increment left pointer to increment and maximize the scores 
        #Decrement with right pointer , to survive and not let the conditions die !
        while l <= r : 
            while l <= r and power >= tokens[l]:
                power = power - tokens[l]
                l += 1
                score += 1 
                maxScore = max(score ,maxScore)
                print("l" , l , power , score)
            
            while l <= r and power < tokens[l]:
                power = power + tokens[r]
                r -= 1 
                score -= 1 
                maxScore = max(score ,maxScore)
                if score < 0 : 
                    #Score can't be negative !
                    return maxScore 
                print("r" , r , power , score)


        return maxScore 

        