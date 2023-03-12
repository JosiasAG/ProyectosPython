import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500")
valor = ""
def bisiesto(casilla):
    try:
        bis = int(casilla.get())
    except ValueError:
        tk.Label(ventana, text="Fecha inválida").pack()
    else:
        if bis % 4 == 0:
            if bis % 100 != 0 or bis % 400 == 0:
                tk.Label(ventana, text=f"El año {bis} es bisiesto").pack()
            else:
                tk.Label(ventana, text=f"El año {bis} no es bisiesto").pack()
        else:
            tk.Label(ventana, text=f"El año {bis} no es bisiesto").pack()


casilla = tk.Entry(ventana)
casilla.pack()

tk.Button(ventana, text="Calcular año bisiesto", command=lambda: bisiesto(casilla)).pack()

tk.mainloop()

