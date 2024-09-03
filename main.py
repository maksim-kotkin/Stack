class Stack:
    def __init__(self):
        self.list = []
        
    def is_empty(self):
        return len(self.list) == 0

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            return None

    def size(self):
        return len(self.list)

def ballance(expression):
    stack = Stack()
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_map.values():
            stack.push(char)
        elif char in bracket_map.keys():
            if stack.is_empty() or stack.pop() != bracket_map[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


expression = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
expression_1 = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]

if __name__ == "__main__":
    for i in expression + expression_1:
        result = ballance(i)
        print(result)
