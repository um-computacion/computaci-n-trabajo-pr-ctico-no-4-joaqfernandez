def factorial(n: int):
    if n == 1: 
        return 1
    else:
        return n * factorial(n - 1)
    

def factorial_recursivo(n:int) ->int:
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)
    

def factorial_no_recursivo(n:int) ->int:
    total = 1
    while n > 0:
        total = total * n
        n = n -1 
    return total