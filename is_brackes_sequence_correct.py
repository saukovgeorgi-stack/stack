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

def is_bracket_sequence_correct(s: str):
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "([":
            _stack.push(brace)
        else:
            assert brace in ")]", "NB there should be a closing bracket here: " + str(brace)
            if _stack.is_empty():
                return False
            left = _stack.pop()
            assert left in "[(", "NB there should be a opening bracket here: " + str(left)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"

            if right != brace:
                return False
    return _stack.is_empty()




print(is_bracket_sequence_correct("(((())))"))
