class Stack:

    def __init__(self):
        self.data = []

    def push(self, element): # append el in the last position
        self.data.append(element)

    def pop(self): # pops the last element
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")

    def top(self):  # top el in stack is the last element
        if not self.is_empty():
            return self.data[-1]
        else:
            return None

    def is_empty(self): # making bool where length of the list is zero if it is True else False
        return len(self.data) == 0

    def __str__(self):
        result = "[" + ", ".join(reversed(self.data)) + "]"
        return result


stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("orange")
print("Stack:", stack)  # Output: [orange, banana, apple]

print("Top element:", stack.top())  # Output: orange

popped_element = stack.pop()
print("Popped element:", popped_element)  # Output: orange

print("Stack after popping:", stack)  # Output: [banana, apple]

print("Is the stack empty?", stack.is_empty())  # Output: False