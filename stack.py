_stack = []

def push(x):
    _stack.append(x)

def pop():
    x = _stack.pop()
    return x
    
def clear():
    _stack.clear()

def is_empty():
    return len(_stack) == 0

def top():
    return _stack[-1]



if __name__ == "__stack__":
    import doctest
    doctest.testmod()
