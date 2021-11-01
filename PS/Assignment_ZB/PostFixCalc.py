class Stack:
    def __init__(self):
        self.list = list()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

class Calculator:
    def __init__(self):
        self.stack = Stack()

       def calculate(self, string):
        for item in string.split(' '):
            if item == '+':
                self.stack.push(self.stack.pop() - self.stack.pop())
            elif item == '-':
                self.stack.push( -self.stack.pop() + self.stack.pop())
            elif item == '*':
                self.stack.push(self.stack.pop() * self.stack.pop())
            elif item == '/':
                self.stack.push(1/self.stack.pop() * self.stack.pop())
            else:
                self.stack.push(int(item))
        return self.stack.pop()

# Test code
calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +'))
print(calc.calculate('2 5 + 3 * 6 - 5 *'))
