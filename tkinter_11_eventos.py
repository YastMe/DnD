'''Iniciación a tkinter.Diciembre 2020.
IFC Castelar TestLab'''

#Comenzamos a usar el alias para reducir algunas líneas
import tkinter as tk




def configurar_ventana(v):
    v.title("Aprendiendo tkinter")
    v.geometry("500x300+50+50")
    #app_icono = tk.PhotoImage(file="res/logoiescastelar.png")
    # v.iconphoto(True, app_icono)
    # v.resizable(width="False", height="False")

#Método a ejecutar cuando se pulsa una tecla. Se recibe en el parámetro event
def mostrar_tecla(event):
    print("Tecla pulsada: "+event.char)

def gestionar_pulsacion_raton(event):
    print("Se ha pulsado el ratón en la posición x: {} y:{}".format(event.x,event.y))

# main
principal = tk.Tk()
configurar_ventana(principal)
label01 = tk.Label(principal,text="Observa el terminal y pulsa alguna tecla")
label01.grid(column=0,row=0,padx=10,pady=10)


#bind nos permite asociar un evento de la ventana tk.Tk() a una función concreta
#Ejemplo: al pulsar una tecla llamamos a la función adecuada para mostrar la tecla
principal.bind("<Key>",mostrar_tecla)
#Al entrar en el mainloop, el sistema permanecerá sensible a las pulsaciones de tecla llamando a la función.

#Otro ejemplo
principal.bind("<Button-1>",gestionar_pulsacion_raton)


principal.mainloop()
