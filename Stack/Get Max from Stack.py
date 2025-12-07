class SpecialStack:

    def __init__(self):
        # Define Stack
        self.stack = []
        self.maxStack= []
    
    def push(self, x):
        # Add an element to the top of Stack
        self.stack.append(x)
        if not self.maxStack:
            self.maxStack.append(x)
        else:
            self.maxStack.append(max(x, self. maxStack[-1]))
    
    def pop(self):
        # Remove the top element from the Stack
        if not self.stack:
            return 
        self.maxStack.pop()
        return self.stack.pop()
    
    def peek(self):
        # Returns top element of Stack
        if not self.stack:
            return -1
        return self.stack[-1]
    
    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack) == 0
    
    def getMax(self):
        # Finds maximum element of Stack
        if not self.stack:
            return -1
        return self.maxStack[-1]