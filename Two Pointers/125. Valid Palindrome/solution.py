class Solution:
    def alphaNum(self, c): #firstly creates a function that will make sure that something is alphanumerical
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
        
    def isPalindrome(self, s: str) -> bool: # function that checks for palindrome 
        l, r = 0, len(s) - 1 #initialize the left and right pointer variables

        while l < r: # while left pointer hasnt reached right pointer's position
            while l < r and not self.alphaNum(s[l]): # while left pointer hasnt reached right pointer's position and left pointer character
                l += 1                               # is alphanumeric, move left pointer to the right by one
            while r > l and not self.alphaNum(s[r]): # while left pointer hasnt reached right pointer's position and right pointer character
                r -= 1                               # is alphanumeric, move right pointer to the left by one
            if s[l].lower() != s[r].lower(): #if the left pointer character is not equal to the right pointer character 
                return False                 # return False
            l, r = l + 1, r - 1 # move left pointer to the right; move right pointer to the left 
        return True # return True if you havent gotten False after going through both strings
    
    
