class MinStack:
    def __init__(self):# constructer
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None: #Push method
        if not self.stack: # if stack is empty
            self.stack.append(0) #append 0
            self.min = x #set min variable to number 
        else:
            self.stack.append(x - self.min) #
            if x < self.min:
                self.min = x

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()
        
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
