class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        print(tokens)
        l ,r = 0 ,len(tokens) - 1
        score = 0 
        maxScore = 0
        #Increment left pointer to increment and maximize the scores 
        #Decrement with right pointer , to survive and not let the conditions die !
        #Good Insight -> 
        #I think one way to put it is to think if there's a necessarily optimal choice (locally optimal that leads to overall optimal) that can always be made, and if so, then a greedy solution should be possible, and is probably more "correct" for the problem. The main reason for using DP, as opposed to greedy, is when locally optimal choices do not necessarily lead to the overall optimal solution. In typical examples of DP problems where you have choices (like take or leave), you don't know whether taking or leaving would lead to the overall optimal solution, because that depends on future iterations / sub-problems, and because of that, you have to use DP to exhaust all possibilities and combinations. In such problems, you would also realize that greedy could lead you down a sub-optimal path very easily since it only accounts for locally optimal solutions, so that's a clear no-no. However, in this problem, you realize after sorting that you can always make an optimal choice (locally optimal but also leads to overall optimal). After sorting, if you have enough power to face-up (gain score, lose power) a token, then it doesn't make much sense to ignore that token, since any other token you consider (after that token) will cost you more power, which already sounds quite sub-optimal (why take the more expensive and leave the cheaper). Similarly, if you have no power, then you should face-down (lose score, gain power) the token with the highest value, because the alternative of ignoring the highest value token, and going to a lesser value token, means you are going to get less power for the score you lose which again, seems quite sub-optimal, and you cannot consider face-up because you don't have enough power for the cheapest token available (remember sorted so no point looking for another token that you might be able to face-up). Really, the problem with greedy algorithms is dealing with the doubt of guaranteed optimality, since the guarantee is only available if the local optimal leads to overall optimal, and that can be challenging to get a feel for, or even prove. This is one of the examples where the overall optimal choice is a bit more obvious, and it is also the locally optimal choice. But of course, there are also plenty of problems where it's very difficult to see why greedy works (why local optimal contributes to overall optimal). By learning about the properties of DP and greedy, when each is appropriate, and by building intuition with practice, you should be able to get a slight feel for when greedy or DP is more appropriate for a problem.
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

        
