while ValueError:
    try:
        n = int(input("Ingresa un número: "))
    except ValueError:
        print("Por favor ingrese una cifra")
    else:
        break

ecuacion = ""

def sumar(n):
    n2 = int(input("Ingrese el segundo valor: "))
    n += n2
    return n

def restar(n):
    n2 = int(input("Ingrese el segundo valor: "))
    n -= n2
    return n

def multiplicacion(n):
    n2 = int(input("Ingrese el segundo valor: "))
    n *= n2
    return n

def division(n):
    n2 = int(input("Ingrese el segundo valor: "))
    n /= n2
    return n

while True:
    ecuacion = input("Operación: suma, resta, mult, div, salir: ")
    if ecuacion == "suma":
        n = sumar(n)
        print(n)
    elif ecuacion == "resta":
        n = restar(n)
        print(n)
    elif ecuacion == "mult":
        n = multiplicacion(n)
        print(n)
    elif ecuacion == "div":
        n = division(n)
        print(n)
    elif ecuacion == "salir":
        break
    else:
        print("Operación invalida, intente de nuevo")
