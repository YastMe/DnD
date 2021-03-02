import tkinter as tk
# import math
from tkinter import ttk
import os


# DEBUG:

def gestionar_pulsacion_raton(event):
    print("Se ha pulsado el ratón en la posición x: {} y:{}".format(event.x, event.y))


def winconfig():
    principal.title("Ficha Python")
    principal.geometry("860x345+200+100")
    principal.resizable(width="False", height="False")
    principal.configure(background='lightgrey')
    principal.bind("<Button-1>", gestionar_pulsacion_raton)


def boton():
    global ListaTk

    f_list = os.listdir("./")

    if "Jugador.txt" in f_list:
        e = open("Jugador.txt", "w", encoding="utf-8")
    else:
        e = open("Jugador.txt", "w", encoding="utf-8")

    for c in range(0, len(ListaTk)):
        if (c % 2) == 0:
            ListaTk[c].set(ListaTk[c + 1].get())
            e.write(ListaTk[c].get() + "\n")

    e.close()
    for n in range(0, 47):
        if ListaRangosAsignados[n].get():
            ListaRangos[n].append(True)
        else:
            ListaRangos[n].append(False)
        ListaRangos[n][3] = 0


def scroll(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


principal = tk.Tk()
winconfig()
principal.bind("<MouseWheel>", scroll)

StatsBase = []
StatsTotal = []
DadosVida = []
ListaRangos = []

f = open("Rangos.txt", "r", encoding="utf-8")

for i in range(0, 48):
    ListaRangos.append(f.readline().split(','))

f.close()

# ListaRangos posiciones:

# [X][0] - Nombre
# [X][1] - Habilidad
# [X][2] - Rangos
# [X][3] - Total
# [X][4] - Clásea

NombreTk = tk.StringVar()
TextoNombre = tk.Label(principal, text="Nombre", anchor='w', relief="groove")
TextoNombre.place(x=10, y=31, width=300)
EntradaNombre = ttk.Entry(principal)
EntradaNombre.place(x=10, y=10, width=300)

JugadorTk = tk.StringVar()
TextoJugador = tk.Label(principal, text="Jugador", anchor='w', relief="groove")
TextoJugador.place(x=320, y=31, width=300)
EntradaJugador = ttk.Entry(principal)
EntradaJugador.place(x=320, y=10, width=300)

ClaseTk = tk.StringVar()
TextoClase = tk.Label(principal, text="Clase", anchor='w', relief="groove")
TextoClase.place(x=10, y=91, width=200)
EntradaClase = ttk.Entry(principal)
EntradaClase.place(x=10, y=70, width=200)

Lv = tk.StringVar()
TextoLv = tk.Label(principal, text="Lv", anchor='w', relief="groove").place(x=220, y=91, width=90)
EntradaLv = ttk.Entry(principal)
EntradaLv.place(x=220, y=70, width=90)

RazaTk = tk.StringVar()
TextoRaza = tk.Label(principal, text="Raza", anchor='w', relief="groove").place(x=320, y=91, width=90)
EntradaRaza = ttk.Entry(principal)
EntradaRaza.place(x=320, y=70, width=90)

AlineamientoTk = tk.StringVar()
TextoAlineamiento = tk.Label(principal, text="Alineamiento", anchor='w', relief="groove").place(x=420, y=91, width=100)
EntradaAlineamiento = ttk.Entry(principal)
EntradaAlineamiento.place(x=420, y=70, width=100)

DeidadTk = tk.StringVar()
TextoDeidad = tk.Label(principal, text="Deidad", anchor='w', relief="groove").place(x=530, y=91, width=90)
EntradaDeidad = ttk.Entry(principal)
EntradaDeidad.place(x=530, y=70, width=90)

TamanioTk = tk.StringVar()
TextoTamanio = tk.Label(principal, text="Tamaño", anchor='w', relief="groove").place(x=10, y=151, width=70)
EntradaTamanio = ttk.Entry(principal)
EntradaTamanio.place(x=10, y=130, width=70)

EdadTk = tk.StringVar()
TextoEdad = tk.Label(principal, text="Edad", anchor='w', relief="groove").place(x=90, y=151, width=50)
EntradaEdad = ttk.Entry(principal)
EntradaEdad.place(x=90, y=130, width=50)

SexoTk = tk.StringVar()
TextoSexo = tk.Label(principal, text="Sexo", anchor='w', relief="groove").place(x=150, y=151, width=60)
EntradaSexo = ttk.Entry(principal)
EntradaSexo.place(x=150, y=130, width=60)

AlturaTk = tk.StringVar()
TextoAltura = tk.Label(principal, text="Altura", anchor='w', relief="groove").place(x=220, y=151, width=90)
EntradaAltura = ttk.Entry(principal)
EntradaAltura.place(x=220, y=130, width=90)

PesoTk = tk.StringVar()
TextoPeso = tk.Label(principal, text="Peso", anchor='w', relief="groove").place(x=320, y=151, width=60)
EntradaPeso = ttk.Entry(principal)
EntradaPeso.place(x=320, y=130, width=60)

OjosTk = tk.StringVar()
TextoOjos = tk.Label(principal, text="Ojos", anchor='w', relief="groove").place(x=390, y=151, width=70)
EntradaOjos = ttk.Entry(principal)
EntradaOjos.place(x=390, y=130, width=70)

CabelloTk = tk.StringVar()
TextoCabello = tk.Label(principal, text="Cabello", anchor='w', relief="groove").place(x=470, y=151, width=70)
EntradaCabello = ttk.Entry(principal)
EntradaCabello.place(x=470, y=130, width=70)

PielTk = tk.StringVar()
TextoPiel = tk.Label(principal, text="Piel", anchor='w', relief="groove").place(x=550, y=151, width=70)
EntradaPiel = ttk.Entry(principal)
EntradaPiel.place(x=550, y=130, width=70)

EXPHTk = tk.StringVar()
TextoEXPH = tk.Label(principal, text="EXPH", anchor='w', relief="groove")#.place(x=10, y=211, width=50)
EntradaEXPH = ttk.Entry(principal)
# EntradaEXPH.place(x=10, y=190, width=50)

CobreTk = tk.StringVar()
TextoCobre = tk.Label(principal, text="Cobre", anchor='w', relief="groove").place(x=10, y=271, width=145)
EntradaCobre = ttk.Entry(principal)
EntradaCobre.place(x=10, y=250, width=145)

PlataTk = tk.StringVar()
TextoPlata = tk.Label(principal, text="Plata", anchor='w', relief="groove").place(x=165, y=271, width=145)
EntradaPlata = ttk.Entry(principal)
EntradaPlata.place(x=165, y=250, width=145)

OroTk = tk.StringVar()
TextoOro = tk.Label(principal, text="Oro", anchor='w', relief="groove").place(x=320, y=271, width=145)
EntradaOro = ttk.Entry(principal)
EntradaOro.place(x=320, y=250, width=145)

PlatinoTk = tk.StringVar()
TextoPlatino = tk.Label(principal, text="Platino", anchor='w', relief="groove").place(x=475, y=271, width=145)
EntradaPlatino = ttk.Entry(principal)
EntradaPlatino.place(x=475, y=250, width=145)

BaBTk = tk.StringVar()
BaBTk.set("Malo")
RefTk = tk.StringVar()
RefTk.set("Bueno")
FortTk = tk.StringVar()
FortTk.set("Bueno")
VolTk = tk.StringVar()
VolTk.set("Bueno")

RangosTk = tk.StringVar()
TextoRangos = tk.Label(principal, text="Rangos", anchor='w', relief="groove").place(x=165, y=211, width=145)
EntradaRangos = ttk.Entry(principal)
EntradaRangos.place(x=165, y=190, width=145)

VidaTk = tk.StringVar()
TextoVida = tk.Label(principal, text="Vida", anchor='w', relief="groove").place(x=10, y=211, width=145)
EntradaVida = ttk.Entry(principal)
EntradaVida.place(x=10, y=190, width=145)

CATk = tk.StringVar()
CAToqTk = tk.StringVar()
CADesTk = tk.StringVar()

VelTk = tk.StringVar()
TextoVel = tk.Label(principal, text="Velocidad", anchor='w', relief="groove").place(x=320, y=211, width=145)
EntradaVel = ttk.Entry(principal)
EntradaVel.place(x=320, y=190, width=145)

DadoGolpeTk = tk.StringVar()
TextoDadoGolpe = tk.Label(principal, text="Dado de Golpe", anchor='w', relief="groove").place(x=475, y=211, width=145)
EntradaDadoGolpe = ttk.Entry(principal)
EntradaDadoGolpe.place(x=475, y=190, width=145)

ListaTk = [NombreTk, EntradaNombre, JugadorTk, EntradaJugador, ClaseTk, EntradaClase, Lv, EntradaLv, RazaTk,
           EntradaRaza, AlineamientoTk, EntradaAlineamiento, DeidadTk, EntradaDeidad, TamanioTk, EntradaTamanio, EdadTk,
           EntradaEdad, SexoTk, EntradaSexo, AlturaTk, EntradaAltura, PesoTk, EntradaPeso, OjosTk, EntradaOjos,
           CabelloTk, EntradaCabello, PielTk, EntradaPiel, EXPHTk, EntradaEXPH, CobreTk, EntradaCobre, PlataTk,
           EntradaPlata, OroTk, EntradaOro, PlatinoTk, EntradaPlatino, RangosTk, EntradaRangos, VidaTk, EntradaVida,
           VelTk, EntradaVel, DadoGolpeTk, EntradaDadoGolpe]

ListaRangosAsignados = []

container = tk.ttk.Frame(principal)
canvas = tk.Canvas(container)
canvas.configure(width=214, height=500)
scrollbar = tk.ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=500, height=1170)
canvas.configure(yscrollcommand=scrollbar.set)

for i in range(0, 47):
    ListaRangosAsignados.append(tk.IntVar())
    tk.Checkbutton(scrollable_frame, text=ListaRangos[i][0], variable=ListaRangosAsignados[i], onvalue=1,
                   offvalue=0, anchor="w").pack(fill='both')

TextoClaseas = tk.Label(principal, text="Habilidades de clase", relief="groove").place(x=685, y=10)

container.place(x=630, y=31, height=260)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.place(x=200, y=0, height=260)

BotonTk = tk.Button(principal, text="EL BOTÓN", command=boton).place(x=370, y=310)

# for i in range(0, 6):
#     StatsBase.append(int(input("Inserta estadística ")))
#     StatsTotal.append(math.floor((StatsBase[i] - 10) / 2))

# VidaTotal = int(DadoGolpeTk.get()) + StatsTotal[2]
# Iniciativa = StatsTotal[1]
# CA = 10 + StatsTotal[1]
# CAToq = 10 + StatsTotal[1]
# CADes = 10

# if RefTk.get() == "Bueno":
#     Ref = 2 + int(Lv.get() / 2) + StatsTotal[1]
# elif RefTk.get() == "Malo":
#     Ref = int(Lv.get() / 3) + StatsTotal[1]
#
# if FortTk.get() == "Bueno":
#     Fort = 2 + int(Lv.get() / 2) + StatsTotal[2]
# elif FortTk.get() == "Malo":
#     Fort = int(Lv.get() / 3) + StatsTotal[2]
#
# if VolTk.get() == "Bueno":
#     Vol = 2 + int(Lv.get() / 2) + StatsTotal[4]
# elif VolTk.get() == "Malo":
#     Vol = int(Lv.get() / 3) + StatsTotal[4]
#
# for i in range(0, Lv.get() - 1):
#     VidaTotal = VidaTotal + int(input()) + StatsTotal[2]
#
# if BaBTk.get() == "Bueno":
#     BaB = Lv.get()
# elif BaBTk.get() == "Regular":
#     BaB = Lv.get() - math.ceil(Lv.get() / 4)
# else:
#     BaB = int(Lv.get() / 2)

principal.mainloop()

print(ListaRangos)

# PREPARASIÓN ACABÁ
