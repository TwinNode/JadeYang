def zero(func=None): 
    if func is None: return 0
    return func(0)
def one(func=None): 
    if func is None: return 1
    return func(1)
def two(func=None): 
    if func is None: return 2
    return func(2)
def three(func=None):
    if func is None: return 3
    return func(3)
def four(func=None): 
    if func is None: return 4
    return func(4)
def five(func=None): 
    if func is None: return 5
    return func(5)
def six(func=None): 
    if func is None: return 6
    return func(6)
def seven(func=None): 
    if func is None: return 7
    return func(7)
def eight(func=None): 
    if func is None: return 8
    return func(8)
def nine(func=None): 
    if func is None: return 9
    return func(9)

def plus(right_num): 
    return lambda left_num : left_num + right_num
def minus(right_num): 
    return lambda left_num : left_num - right_num
def times(right_num): 
    return lambda left_num : left_num * right_num
def divided_by(right_num): 
    if right_num == 0:
        return lambda left_num : "Cannot divide by zero"
    return lambda left_num : left_num // right_num


#best practice -----------------------------
def identity(a): return a

def zero(f=identity): return f(0)
def one(f=identity): return f(1)
def two(f=identity): return f(2)
def three(f=identity): return f(3)
def four(f=identity): return f(4)
def five(f=identity): return f(5)
def six(f=identity): return f(6)
def seven(f=identity): return f(7)
def eight(f=identity): return f(8)
def nine(f=identity): return f(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b
