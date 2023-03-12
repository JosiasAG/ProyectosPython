
def mostrarpreciofinal(precio, descuento):
    precioFinal = (precio - (precio * (descuento/100)))
    return precioFinal

producto = input("Ingrese el nombre del producto: ")
precio = int(input("ingrese el precio: "))
descuento = int(input("Ingrese el descuento: "))
precioFinal = mostrarpreciofinal(precio, descuento)

print("El precio del " + str(producto) + " es de " + str(precioFinal) + " con un descuento del " + str(descuento) + "%, gracias, que vuelva pronto")



