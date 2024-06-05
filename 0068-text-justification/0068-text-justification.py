class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line , length = []  , 0 
        res = []
        i = 0 

        # length -> length of words without spaces 
        # len(line) - 1 -> Accounts for spaces between words 
        # len(words[i]) -> length of the word
        while i < len(words):
            #When line goes out of maxWidht 
            #if statement does not work for ascertaining last line 
            if length + len(line) + len(words[i]) > maxWidth : 
                #Line complete 

                extra_spaces = maxWidth - length

                #max of 1 is taken to have division 
                #Distrube evenly 
                spaces = extra_spaces // max(1 , len(line) - 1)
                #Distribute greedily and evenly 
                remainder = extra_spaces % max(1 , len(line) - 1)

                #remainder will be exhausted , by the time loop runs 
                for j in range(max(1 , len(line) - 1)):
                    line[j] += " " * spaces 
                    if remainder : 
                        line[j] += " "
                        remainder -= 1 

                #Append the line and re do the work 
                res.append("".join(line))
                line , length = [] , 0
            
            line.append(words[i])
            length += len(words[i])
            i += 1 
        
        #Handling last line which was not handled in if case !
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)
        return res 
