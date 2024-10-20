class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s) != len(t): #if both strings are not the same length, they can't be anagrams
            return False

        count = [0] * 26 #makes a list of 26 zeros(one for each letter); ord gives the unicode value of a letter 
        for i in range(len(s)):   # for each letter in string s 
            count[ord(s[i]) - ord('a')] += 1 # using ord to find the position of the encountered letter(from string s) in the count list 
            # and increasing by  1 
            count[ord(t[i]) - ord('a')] -= 1 # using ord to find the position of the encountered letter(from string t) in the count list 
            # and decreasing by 1 
            
        #by the end of this, if there are an equal amount of encounters for letters in both strings, they should cancel out and 
        #the list should have no values except 0

        for val in count: #for each value in count, if the value doesn't equal 0, return FALSE
            if val != 0:
                return False
                
        return True #return TRUE otherwise


#Time Complexity: O(n)
#Space Complexity: O(1)
