def calculate(operation, x, y):
    if operation == 'Addition':
        return x+y
    elif operation == 'Subtraction':
        if x>y:
            return x-y
        else:
            return y-x
    elif operation == 'Multiplication':
        return x*y
    elif operation == 'Division':
        return x/y