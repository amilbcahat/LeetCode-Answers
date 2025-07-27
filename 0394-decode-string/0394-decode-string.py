class Solution:
    def decodeString(self, s: str) -> str:

        def recur(idx): 
            multiplier = 0 
            decoded_str = '' 

            while idx < len(s) and s[idx] != ']': 
                if s[idx].isdigit(): 
                    multiplier = 10 * multiplier + int(s[idx])

                elif s[idx] == "[": 
                    decoded_str_returned, idx_of_closed_next = recur(idx + 1)
                    decoded_str += multiplier * decoded_str_returned
                    multiplier = 0 

                    idx = idx_of_closed_next
                else: 
                    decoded_str += s[idx]
                
                idx += 1

            return decoded_str, idx

        return recur(0)[0]