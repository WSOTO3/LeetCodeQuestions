class MinStack:
    def __init__(self):# constructer
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None: # Push method
        if not self.stack: # if stack is empty
            self.stack.append(0) # append 0
            self.min = x # set min variable to number 
        else:
            self.stack.append(x - self.min) # append x number minus minimum
            if x < self.min: # if x is less than min
                self.min = x # new min is x 

    def pop(self) -> None: # pop methos
        if not self.stack: # if empty, return
            return
        
        pop = self.stack.pop()  # pop equals stack pop
        
        if pop < 0: # if pop is less than 0 
            self.min = self.min - pop # min is now min minus pop 

    def top(self) -> int: # top method
        top = self.stack[-1] # top is last index in stack
        if top > 0: # if top is more than 0
            return top + self.min # return top + min
        else:
            return self.min # return min

    def getMin(self) -> int:# min method
        return self.min # return min
