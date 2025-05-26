class Codec:
    def encode(self, strs):
        # StringBuilder to build the encoded string
        encoded_string = []

        # Iterate through each string in the list
        for s in strs:
            # Append the length of the string followed by a '#' separator
            encoded_string.append(f"{len(s)}#{s}")
            # The length helps in decoding the exact number of characters for each string
        # Return the final encoded string containing all strings in the desired format
        return ''.join(encoded_string)

    # Function to decode the single string back to a list of strings
    def decode(self, s):
        strs = []
        i = 0

        # Process the encoded string until all characters are decoded
        while i < len(s):
            # Find the position of the next '#' separator
            j = s.find('#', i)
            # Extract the length of the next string using the substring before '#'
            length = int(s[i:j])
            # Extract the actual string using the calculated length
            strs.append(s[j + 1:j + 1 + length])
            # Move the pointer to the next encoded string part
            i = j + 1 + length
        # Return the decoded list of strings
        return strs
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))