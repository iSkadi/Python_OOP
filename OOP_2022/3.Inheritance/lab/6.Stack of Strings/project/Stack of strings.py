class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1] #последния елемент " reference to the topmost element of the stack

    def is_empty(self):
        return len(self.data) == 0 # връща True ili Falce

# •	Override the string method to return the stack data in the format:
    # "[{element(N)}, {element(N-1)} ... {element(0)}]"

    def __str__(self):
        return "[" + ', '.join(reversed(self.data)) + "]"



