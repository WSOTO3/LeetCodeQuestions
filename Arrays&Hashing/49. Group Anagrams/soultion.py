class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams; defaultdict so when a key does not exist yet it doesnt give us an error 
        
        for s in strs: # for every string in list of strings
            count = [0] * 26 # we will layout the 0s for each character a .....z every letter starts with 0 
            
            for c in s: #for each character in the string
                count[ord(c) - ord("a")] += 1 # the count/occurence of that certain character goes up by 1; ord is using the ascii value of
                                              # the character minus the ascii character of lower case a to get the index in count that should
                                              # go up  
                
            res[tuple(count)].append(s) # append that string as a value to the specific count key in the result dictionary; made count into a
                                        # tuple since lists cannot be keys  *basically makes the tuple of 0s/1s a key and appends any word that
                                        # matches with that as a value
        
        print(res)    
        return list(res.values())
    

        # Time Complexity: O(m * n)
        # Space Complexity (m)
        # Hash Table
