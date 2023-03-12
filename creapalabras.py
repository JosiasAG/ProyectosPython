import random

consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
            'v', 'w', 'x', 'y', 'z']

vocales =["a", "e", "i", "o", "u"]

cuenta = random.randrange(2, 4)
palabra = ""
regresion = 100

lista = []

while regresion > 0:
    for i in range(cuenta):
        numero = random.choice(consonantes)
        numero2 = numero + random.choice(vocales)
        palabra += numero2
    lista.append(palabra)
    cuenta = random.randrange(3, 5)
    palabra = ""
    regresion -= 1

for i in lista:
    print(i, end=", ")

