
palabra = input("Escribe una frase: ")
palabra = palabra.title()
separador = palabra.split()

for i in separador:
    mayuscula = i[0]
    if i != "De":
        print(mayuscula, end=".")
