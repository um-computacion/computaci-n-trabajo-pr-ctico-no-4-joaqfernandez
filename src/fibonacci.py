def fibonacci(n:int):
    f0 = 0
    f1= 1
    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_iterativo(n:int):
    f0 = 0 
    f1 = 1
    if n == 0:
        return f0
    elif n == 1:
        return f1
    
    a, b = f0, f1 
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

try:
    n= int(input("Ingrese un número entero positivo: "))
    resultado = fibonacci_iterativo(n)
    print(f"el resultado es: {resultado}")
except ValueError:
    print("debes ingresar un numero valido")