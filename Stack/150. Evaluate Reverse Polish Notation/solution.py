class Solution: # solution class
    def evalRPN(self, tokens: List[str]) -> int: 
        stack = [] 
        for c in tokens: # for each character in the list of tokens
            if c == "+": # if it's a plus
                stack.append(stack.pop() + stack.pop()) # append the sum of the next two pops 
            elif c == "-": # if its a minus
                a, b = stack.pop(), stack.pop() # a nd b are the next two pops 
                stack.append(b - a) # append the difference 
            elif c == "*": # if its multipy
                stack.append(stack.pop() * stack.pop()) # append the product of the next two pops 
            elif c == "/": # if divide 
                a, b = stack.pop(), stack.pop() # a and b are the next two pops 
                stack.append(int(float(b) / a)) # append the quotient 
            else: # if its a number, append it to the stack 
                stack.append(int(c))
        return stack[0] # return stack 
