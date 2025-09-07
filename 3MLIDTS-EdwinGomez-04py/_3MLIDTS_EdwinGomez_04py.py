## Formulario de registro almacenamiento en TXT sin validación
import tkinter as tk
from tkinter import messagebox
### Definición de funciones
def  limpiar_campos():
    txtNombre.delete(0,tk.END)
    txtApellido.delete(0,tk.END)
    txtEdad.delete(0,tk.END)
    txtEstatura.delete(0,tk.END)
    txtTelefono.delete(0,tk.END)
    var_genero.set(0)
def borrar_fun():
    limpiar_campos()
def guardar_valores():
    #Obtener valores desde las entrys
    nombre=txtNombre.get()
    apellidos=txtApellido.get()
    edad=txtEdad.get()
    estatura=txtEstatura.get()
    telefono=txtTelefono.get()
    ###Obtner el genero de los RadioButtons
    genero =""
    if var_genero.get()==1:
        genero="Hombre"
    elif var_genero.get()==2:
        genero= "Mujer"
    ###Generar la cadena de carateres 
    datos= "Nombres: "+nombre+"\n"+"Apellidos"+apellidos+"\n"+"Edad: "+edad+"anos\n"+"Estatura: "+estatura+"\n"+"Telefons: "+telefono
    ###Guardar los datos en el archivo TXT
    with open("3M2025Datos.txt","a") as archivo:
         archivo.write(datos+"\n\n")
    ###Mostrar mensaje de confirmacón
    messagebox.showinfo("Informacion","Datos guardados con exito: \n\n"+datos)
    txtNombre.delete(0,tk.END)
    txtApellido.de1ete(0,tk.END)
    txtEdad.delete(0,tk.END)
    txtEstatura.delete(0,tk.END)
    txtTelefono.delete(0,tk.END)
    var_genero.set(0)

ventana = tk.Tk()
ventana.geometry("420x400")
ventana.title("Formulario de registro")
ventana.configure(bg="lightblue")
var_genero = tk.IntVar()

lblNombre = tk.Label(ventana, text="Nombre: ")
lblNombre.pack()
txtNombre= tk.Entry()
txtNombre.pack()
lblApellido = tk.Label(ventana, text = "Apellidos: ")
lblApellido.pack()
txtApellido = tk.Entry()
txtApellido.pack()
lblTel = tk.Label(ventana, text = "Telefono: ")
lblTel.pack()
txtTelefono = tk.Entry()
txtTelefono.pack()
lblAge = tk.Label(ventana, text = "Edad: ")
lblAge.pack()
txtEdad = tk.Entry()
txtEdad.pack()
lbEsta = tk.Label(ventana, text = "Estatura: ")
lbEsta.pack()
txtEstatura = tk.Entry()
txtEstatura.pack()
lblGen = tk.Label(ventana, text="Sexo")
lblGen.pack

rbMan = tk.Radiobutton(ventana, text = "Hombre", variable=var_genero, value=1)
rbMan.pack()
rbWom = tk.Radiobutton(ventana, text = "Mujer", variable=var_genero,value=2)
rbWom.pack()

btnBorrar = tk.Button(ventana, text="Borrar", command=borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()

ventana.mainloop()


