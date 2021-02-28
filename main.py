import tkinter as tk
import math
from tkinter import ttk


def winconfig():
    principal.title("Ficha Python")
    principal.geometry("1280x720+200+100")
    principal.resizable(width="True", height="True")


def boton():

    global NombreTk, EntradaNombre, JugadorTk, EntradaJugador, ClaseTk, EntradaClase, Lv, EntradaLv, RazaTk, \
        EntradaRaza, AlineamientoTk, EntradaAlineamiento, DeidadTk, EntradaDeidad, TamanioTk, EntradaTamanio, EdadTk, \
        EntradaEdad, SexoTk, EntradaSexo, AlturaTk, EntradaAltura, PesoTk, EntradaPeso, OjosTk, EntradaOjos, \
        CabelloTk, EntradaCabello, PielTk, EntradaPiel, EXPHTk, EntradaEXPH, CobreTk, EntradaCobre, PlataTk, \
        EntradaPlata, OroTk, EntradaOro, PlatinoTk, EntradaPlatino, RangosTk, EntradaRangos, VidaTk, EntradaVida, \
        VelTk, EntradaVel, DadoGolpeTk, EntradaDadoGolpe

    NombreTk = EntradaNombre.get()
    JugadorTk = EntradaJugador.get()
    ClaseTk = EntradaClase.get()
    Lv = EntradaLv.get()
    RazaTk = EntradaRaza.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()
    NombreTk = EntradaNombre.get()

principal = tk.Tk()
winconfig()

StatsBase = []
StatsTotal = []
DadosVida = []
ListaRangos = []

f = open("Rangos.txt", "r", encoding="utf-8")

for i in range(0, 48):
    ListaRangos.append(f.readline().split(','))

print(ListaRangos[2])

# ListaRangos posiciones:

# [X][0] - Nombre
# [X][1] - Habilidad
# [X][2] - Rangos
# [X][3] - Total

NombreTk = tk.StringVar()
TextoNombre = tk.Label(principal, text="Nombre").pack()
EntradaNombre = ttk.Entry(principal).pack()

JugadorTk = tk.StringVar()
TextoJugador = tk.Label(principal, text="Jugador").pack()
EntradaJugador = ttk.Entry(principal).pack()

ClaseTk = tk.StringVar()
TextoClase = tk.Label(principal, text="Clase").pack()
EntradaClase = ttk.Entry(principal).pack()

Lv = tk.IntVar()
TextoLv = tk.Label(principal, text="Lv").pack()
EntradaLv = ttk.Entry(principal).pack()

RazaTk = tk.StringVar()
TextoRaza = tk.Label(principal, text="Raza").pack()
EntradaRaza = ttk.Entry(principal).pack()

AlineamientoTk = tk.StringVar()
TextoAlineamiento = tk.Label(principal, text="Alineamiento").pack()
EntradaAlineamiento = ttk.Entry(principal).pack()

DeidadTk = tk.StringVar()
TextoDeidad = tk.Label(principal, text="Deidad").pack()
EntradaDeidad = ttk.Entry(principal).pack()

TamanioTk = tk.StringVar()
TextoTamanio = tk.Label(principal, text="Tamaño").pack()
EntradaTamanio = ttk.Entry(principal).pack()

EdadTk = tk.StringVar()
TextoEdad = tk.Label(principal, text="Edad").pack()
EntradaEdad = ttk.Entry(principal).pack()

SexoTk = tk.StringVar()
TextoSexo = tk.Label(principal, text="Sexo").pack()
EntradaSexo = ttk.Entry(principal).pack()

AlturaTk = tk.StringVar()
TextoAltura = tk.Label(principal, text="Altura").pack()
EntradaAltura = ttk.Entry(principal).pack()

PesoTk = tk.StringVar()
TextoPeso = tk.Label(principal, text="Peso").pack()
EntradaPeso = ttk.Entry(principal).pack()

OjosTk = tk.StringVar()
TextoOjos = tk.Label(principal, text="Ojos").pack()
EntradaOjos = ttk.Entry(principal).pack()

CabelloTk = tk.StringVar()
TextoCabello = tk.Label(principal, text="Cabello").pack()
EntradaCabello = ttk.Entry(principal).pack()

PielTk = tk.StringVar()
TextoPiel = tk.Label(principal, text="Piel").pack()
EntradaPiel = ttk.Entry(principal).pack()

EXPHTk = tk.IntVar()
TextoEXPH = tk.Label(principal, text="EXPH").pack()
EntradaEXPH = ttk.Entry(principal).pack()

CobreTk = tk.IntVar()
TextoCobre = tk.Label(principal, text="Cobre").pack()
EntradaCobre = ttk.Entry(principal).pack()

PlataTk = tk.IntVar()
TextoPlata = tk.Label(principal, text="Plata").pack()
EntradaPlata = ttk.Entry(principal).pack()

OroTk = tk.IntVar()
TextoOro = tk.Label(principal, text="Oro").pack()
EntradaOro = ttk.Entry(principal).pack()

PlatinoTk = tk.IntVar()
TextoPlatino = tk.Label(principal, text="Platino").pack()
EntradaPlatino = ttk.Entry(principal).pack()

BaBTk = tk.StringVar()
BaBTk.set("Malo")
RefTk = tk.StringVar()
RefTk.set("Bueno")
FortTk = tk.StringVar()
FortTk.set("Bueno")
VolTk = tk.StringVar()
VolTk.set("Bueno")

RangosTk = tk.IntVar()
TextoRangos = tk.Label(principal, text="Rangos").pack()
EntradaRangos = ttk.Entry(principal).pack()

VidaTk = tk.IntVar()
TextoVida = tk.Label(principal, text="Vida").pack()
EntradaVida = ttk.Entry(principal).pack()

CATk = tk.IntVar()
CAToqTk = tk.IntVar()
CADesTk = tk.IntVar()

VelTk = tk.IntVar()
TextoVel = tk.Label(principal, text="Velocidad").pack()
EntradaVel = ttk.Entry(principal).pack()

DadoGolpeTk = tk.IntVar()
TextoDadoGolpe = tk.Label(principal, text="Dado de Golpe").pack()
EntradaDadoGolpe = ttk.Entry(principal).pack()

BotonTk = tk.Button(text="EL BOTÓN").place(x=50, y=50)

for i in range(0, 6):
    StatsBase.append(int(input("Inserta estadística ")))
    StatsTotal.append(math.floor((StatsBase[i] - 10) / 2))

VidaTotal = DadoGolpeTk.get() + StatsTotal[2]
Iniciativa = StatsTotal[1]
CA = 10 + StatsTotal[1]
CAToq = 10 + StatsTotal[1]
CADes = 10

if RefTk.get() == "Bueno":
    Ref = 2 + int(Lv.get() / 2) + StatsTotal[1]
elif RefTk.get() == "Malo":
    Ref = int(Lv.get() / 3) + StatsTotal[1]

if FortTk.get() == "Bueno":
    Fort = 2 + int(Lv.get() / 2) + StatsTotal[2]
elif FortTk.get() == "Malo":
    Fort = int(Lv.get() / 3) + StatsTotal[2]

if VolTk.get() == "Bueno":
    Vol = 2 + int(Lv.get() / 2) + StatsTotal[4]
elif VolTk.get() == "Malo":
    Vol = int(Lv.get() / 3) + StatsTotal[4]

for i in range(0, Lv.get() - 1):
    VidaTotal = VidaTotal + int(input()) + StatsTotal[2]

if BaBTk.get() == "Bueno":
    BaB = Lv.get()
elif BaBTk.get() == "Regular":
    BaB = Lv.get() - math.ceil(Lv.get() / 4)
else:
    BaB = int(Lv.get() / 2)

print(BaB)
print(VidaTotal)
print(StatsBase)
print(StatsTotal)

principal.mainloop()
