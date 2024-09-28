from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x250")
ventana.resizable(False, False)

fondo = PhotoImage("background.png")
fondo_label = Label(ventana, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

def sumar():
    try:
        resultado = float(valor1.get()) + float(valor2.get())
        messagebox.showinfo("Resultado", "La suma es: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def restar():
    try:
        resultado = float(valor1.get()) - float(valor2.get())
        messagebox.showinfo("Resultado", "La resta es: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def multiplicar():
    try:
        resultado = float(valor1.get()) * float(valor2.get())
        messagebox.showinfo("Resultado", "La multiplicación es: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def dividir():
    try:
        resultado = float(valor1.get()) / float(valor2.get())
        messagebox.showinfo("Resultado", "La división es: " + str(resultado))
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

valor1 = Entry(ventana)
valor1.pack(pady=10, padx=20, fill=X)

valor2 = Entry(ventana)
valor2.pack(pady=10, padx=20, fill=X)

boton_suma = Button(ventana, text="Suma", command=sumar, bg="#BF7339", fg="white")
boton_suma.pack(side=LEFT, padx=10, pady=10)

boton_resta = Button(ventana, text="Resta", command=restar, bg="#FAC64B", fg="white")
boton_resta.pack(side=LEFT, padx=10, pady=10)

boton_multiplicacion = Button(ventana, text="Multiplicación", command=multiplicar, bg="#FAA958", fg="white")
boton_multiplicacion.pack(side=LEFT, padx=10, pady=10)

boton_division = Button(ventana, text="División", command=dividir, bg="#C75A0C", fg="white")
boton_division.pack(side=LEFT, padx=10, pady=10)

ventana.mainloop()

