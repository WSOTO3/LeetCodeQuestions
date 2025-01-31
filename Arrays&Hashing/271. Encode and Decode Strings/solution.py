class Solution:
    
    def encode(self, strs: List[str]) -> str: #encodes the strings by adding the number for the length of the string and "#" before it and 
                                              #adding all strings together with no space
        res = ""                              #example: ["cold", "hot"] -> 4#cold3#hot
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]: # undos the encode function
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
