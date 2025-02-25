class Solution:
    def isValid(self, s: str) -> bool: 
        stack = [] #create a stack
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } # Create a dictionary with a close bracket being the keys and 
                                                          # the open brackets being the value
        for c in s: # for each character in the string
            if c in closeToOpen: # if character is one of the brackets:
                if stack and stack[-1] == closeToOpen[c]: # if stack is not empty and the character in the last index of stack is equal to 
                                                          # the closing bracket to the current character 
                  stack.pop() # pop the stack 
                else: 
                    return False # if stack is empty or the last index of stack isnt the closing bracket for current character; return false
            else: # if character is not one of the brackets
                stack.append(c) # append character to stack
        
        return True if not stack else False # return True if stack becomes empty and we havent returned false by end
