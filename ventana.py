from usuario import Usuario
from calculadora import Calculadora
import tkinter as ventana
from datetime import datetime

# zona de ventana

obj_ventana = ventana.Tk()
obj_ventana.geometry("500x550")
obj_ventana.config(bg="blue")
obj_ventana.resizable(False,False)
obj_ventana.title("Calculadora y registro")

# variables globales 
Usuario_actual = None

# sección 1 registro usuario

titulo_label = ventana.Label(obj_ventana,
                             text="registrar usuario",
                             bg="black",
                             fg="white",
                             font=("Arial", 12, "bold"),
                             padx=10,
                             pady=10)
titulo_label.pack(fill="x")

# interfas de sección 1

seccion1 = ventana.Frame(obj_ventana)
seccion1.config(bg="lightblue")
seccion1.pack(pady=10)

# ID del usuario 
label_id = ventana.Label(seccion1, text="ID usauario:", bg="lightblue", font=("Arial", 10))
label_id.grid(row=0, column=0, padx= 10, pady=5)
entry_id = ventana.Entry(seccion1, width=20)
entry_id.grid(row=0, column=1, padx=10 ,pady=5)

# Nombre del usuario

label_nombre = ventana.Label(seccion1, text="Nombre:" ,bg="lightblue", font=("Arial", 10))
label_nombre.grid(row=1, column=0, padx=10, pady=5)
entry_nombre = ventana.Entry(seccion1, width=20)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

# etiqueta de pantalla muestra el usauario registrado
label_usuario_registrado = ventana.Label(obj_ventana, text="Usuario: no registrado", bg="lightblue", font=("Arial", 9))
label_usuario_registrado.pack(fill="x", padx=10, pady=5)

def registro_usuario():
    global Usuario_actual
    id_usuario = entry_id.get()
    nombre_usuario = entry_nombre.get()
    
    if id_usuario and nombre_usuario:
        Usuario_actual = Usuario(id_usuario,nombre_usuario)
        label_usuario_registrado.config(text=f"Usuario: {nombre_usuario} (ID: {id_usuario})")
        entry_id.delete(0, ventana.END)
        entry_nombre.delete(0, ventana.END)
    else:
        label_usuario_registrado.config(text="Usuario: complete los campos", fg="red")
        
boton_registro = ventana.Button(seccion1, text="registrar usuario", command= registro_usuario, bg="black", fg="white", padx=10, pady=5)
boton_registro.grid(row=2, column=0, columnspan=2, pady=10)


# sección 2 calculadora:

titulo_label2 = ventana.Label(obj_ventana,
                              text="Calculadora",
                              bg="black",
                              fg="white",
                              font=("Arial", 12, "bold"),
                              padx=10,
                              pady=10)
titulo_label2.pack(fill="x")

# interfas de sección 2

seccion2 = ventana.Frame(obj_ventana)
seccion2.config(bg="lightblue")
seccion2.pack(pady=10)       
        
# primer numero ingresado por usuario

label_num1 = ventana.Label(seccion2, text="numero 1:", bg="lightblue", font=("Arial", 10))
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = ventana.Entry(seccion2, width=20)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

# segundo numero ingresado por el usario

label_num2 = ventana.Label(seccion2, text="numero 2:", bg="lightblue", font=("Arial", 10))
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = ventana.Entry(seccion2, width=20)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

#resultado

label_resultado = ventana.Label(seccion2, text="Resultado:", bg="lightblue", font=("Arial", 10))
label_resultado.grid(row=2, column=0, padx=10, pady=5)
entry_resultado = ventana.Entry(seccion2, width=20)
entry_resultado.grid(row=2, column=1, padx=10, pady=5)

boton_ope = ventana.Frame(seccion2, bg=("lightblue"))
boton_ope.grid(row=3, column=0, columnspan=2, pady=15)


def realizar_calculo(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        calc = Calculadora(operacion, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        calc.realizar_operacion(num1, num2)
        
        entry_resultado.config(state="normal")
        entry_resultado.delete(0, ventana.END)
        entry_resultado.insert(0, str(calc.get_resultado()))
        entry_resultado.config(state="readonly")
        
        #guardar archivo si hay usuario registrado
        
        if Usuario_actual:
            calc.guardar_info(calc)
            
    except ValueError:
        entry_resultado.config(state="normal")
        entry_resultado.delete(0, ventana.END)
        entry_resultado.insert(0, "Error: numeros invalidos")
        entry_resultado.config(state="readonly", font=("Arial", 10, "bold"), fg="red")

#botones de cada operacion

boton_suma = ventana.Button(boton_ope, text="SUMA +", command=lambda: realizar_calculo("suma"), bg="grey", padx=10, pady=5)
boton_suma.grid(row=0, column=0, padx=5)

boton_resta = ventana.Button(boton_ope, text="RESTA -", command=lambda: realizar_calculo("resta"), bg="grey", padx=10, pady=5)
boton_resta.grid(row=0, column=1, padx=5)

boton_multi = ventana.Button(boton_ope, text="MULTIPLICACION x", command=lambda: realizar_calculo("multiplicacion"), bg="grey", padx=10, pady=5)
boton_multi.grid(row=1, column=0, padx=5, pady=5)

boton_divi = ventana.Button(boton_ope, text="DIVISION /", command=lambda: realizar_calculo("division"), bg="grey", padx=10, pady=5)
boton_divi.grid(row=1, column=1, padx=5, pady=5)
    
#doton limpiar

def limpiar():
    entry_num1.delete(0, ventana.END)
    entry_num2.delete(0, ventana.END)
    entry_resultado.config(state="normal")
    entry_resultado.delete(0, ventana.END)
    entry_resultado.config(state="readonly")
    
doton_limpiar = ventana.Button(seccion2, text="limpiar", command=limpiar, bg="red", fg="white", padx=10, pady=5) 
doton_limpiar.grid(row=4, column=0, columnspan=2, pady=10)   
  
# ejecucion

obj_ventana.mainloop()
