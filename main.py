import tkinter as tk
import math
from tkinter import ttk
import os


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

    NombreTk.set(EntradaNombre.get())
    JugadorTk.set(EntradaJugador.get())
    ClaseTk.set(EntradaClase.get())
    Lv.set(EntradaLv.get())
    RazaTk.set(EntradaRaza.get())
    AlineamientoTk.set(EntradaAlineamiento.get())
    DeidadTk.set(EntradaDeidad.get())
    TamanioTk.set(EntradaTamanio.get())
    EdadTk.set(EntradaEdad.get())
    SexoTk.set(EntradaSexo.get())
    AlturaTk.set(EntradaAltura.get())
    PesoTk.set(EntradaPeso.get())
    OjosTk.set(EntradaOjos.get())
    CabelloTk.set(EntradaCabello.get())
    PielTk.set(EntradaPiel.get())
    EXPHTk.set(EntradaEXPH.get())
    CobreTk.set(EntradaCobre.get())
    PlataTk.set(EntradaPlata.get())
    OroTk.set(EntradaOro.get())
    PlatinoTk.set(EntradaPlatino.get())
    RangosTk.set(EntradaRangos.get())
    VidaTk.set(EntradaVida.get())
    VelTk.set(EntradaVel.get())
    DadoGolpeTk.set(EntradaDadoGolpe.get())

    f_list = os.listdir("./")

    if "Jugador.txt" in f_list:
        f = open("Jugador.txt", "w", encoding="utf-8")
    else:
        f = open("Jugador.txt", "w", encoding="utf-8")

    ListaGuardar = [NombreTk.get(), JugadorTk.get(), ClaseTk.get(), Lv.get(), RazaTk.get(), AlineamientoTk.get(),
                    DeidadTk.get(), TamanioTk.get(), EdadTk.get(), SexoTk.get(), AlturaTk.get(), PesoTk.get(),
                    OjosTk.get(),
                    CabelloTk.get(), PielTk.get(), EXPHTk.get(), CobreTk.get(), PlataTk.get(), OroTk.get(),
                    PlatinoTk.get(),
                    RangosTk.get(), VidaTk.get(), VelTk.get(), DadoGolpeTk.get()]

    f.writelines("%s\n" % item for item in ListaGuardar)
    f.close()


principal = tk.Tk()
winconfig()

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

NombreTk = tk.StringVar()
TextoNombre = tk.Label(principal, text="Nombre")
TextoNombre.grid(row=1, column=1)
EntradaNombre = ttk.Entry(principal)
EntradaNombre.grid(row=2, column=1)

JugadorTk = tk.StringVar()
TextoJugador = tk.Label(principal, text="Jugador")
TextoJugador.grid(row=1, column=2)
EntradaJugador = ttk.Entry(principal)
EntradaJugador.grid(row=2, column=2)

ClaseTk = tk.StringVar()
TextoClase = tk.Label(principal, text="Clase")
TextoClase.grid(row=1, column=3)
EntradaClase = ttk.Entry(principal)
EntradaClase.grid(row=2, column=3)

Lv = tk.StringVar()
TextoLv = tk.Label(principal, text="Lv").grid(row=1, column=4)
EntradaLv = ttk.Entry(principal)
EntradaLv.grid(row=2, column=4)

RazaTk = tk.StringVar()
TextoRaza = tk.Label(principal, text="Raza").grid(row=1, column=5)
EntradaRaza = ttk.Entry(principal)
EntradaRaza.grid(row=2, column=5)

AlineamientoTk = tk.StringVar()
TextoAlineamiento = tk.Label(principal, text="Alineamiento").grid(row=1, column=6)
EntradaAlineamiento = ttk.Entry(principal)
EntradaAlineamiento.grid(row=2, column=6)

DeidadTk = tk.StringVar()
TextoDeidad = tk.Label(principal, text="Deidad").grid(row=1, column=7)
EntradaDeidad = ttk.Entry(principal)
EntradaDeidad.grid(row=2, column=7)

TamanioTk = tk.StringVar()
TextoTamanio = tk.Label(principal, text="Tamaño").grid(row=1, column=8)
EntradaTamanio = ttk.Entry(principal)
EntradaTamanio.grid(row=2, column=8)

EdadTk = tk.StringVar()
TextoEdad = tk.Label(principal, text="Edad").grid(row=1, column=9)
EntradaEdad = ttk.Entry(principal)
EntradaEdad.grid(row=2, column=9)

SexoTk = tk.StringVar()
TextoSexo = tk.Label(principal, text="Sexo").grid(row=3, column=1)
EntradaSexo = ttk.Entry(principal)
EntradaSexo.grid(row=4, column=1)

AlturaTk = tk.StringVar()
TextoAltura = tk.Label(principal, text="Altura").grid(row=3, column=2)
EntradaAltura = ttk.Entry(principal)
EntradaAltura.grid(row=4, column=2)

PesoTk = tk.StringVar()
TextoPeso = tk.Label(principal, text="Peso").grid(row=3, column=3)
EntradaPeso = ttk.Entry(principal)
EntradaPeso.grid(row=4, column=3)

OjosTk = tk.StringVar()
TextoOjos = tk.Label(principal, text="Ojos").grid(row=3, column=4)
EntradaOjos = ttk.Entry(principal)
EntradaOjos.grid(row=4, column=4)

CabelloTk = tk.StringVar()
TextoCabello = tk.Label(principal, text="Cabello").grid(row=3, column=5)
EntradaCabello = ttk.Entry(principal)
EntradaCabello.grid(row=4, column=5)

PielTk = tk.StringVar()
TextoPiel = tk.Label(principal, text="Piel").grid(row=3, column=6)
EntradaPiel = ttk.Entry(principal)
EntradaPiel.grid(row=4, column=6)

EXPHTk = tk.StringVar()
TextoEXPH = tk.Label(principal, text="EXPH").grid(row=3, column=7)
EntradaEXPH = ttk.Entry(principal)
EntradaEXPH.grid(row=4, column=7)

CobreTk = tk.StringVar()
TextoCobre = tk.Label(principal, text="Cobre").grid(row=3, column=8)
EntradaCobre = ttk.Entry(principal)
EntradaCobre.grid(row=4, column=8)

PlataTk = tk.StringVar()
TextoPlata = tk.Label(principal, text="Plata").grid(row=3, column=9)
EntradaPlata = ttk.Entry(principal)
EntradaPlata.grid(row=4, column=9)

OroTk = tk.StringVar()
TextoOro = tk.Label(principal, text="Oro").grid(row=5, column=1)
EntradaOro = ttk.Entry(principal)
EntradaOro.grid(row=6, column=1)

PlatinoTk = tk.StringVar()
TextoPlatino = tk.Label(principal, text="Platino").grid(row=5, column=2)
EntradaPlatino = ttk.Entry(principal)
EntradaPlatino.grid(row=6, column=2)

BaBTk = tk.StringVar()
BaBTk.set("Malo")
RefTk = tk.StringVar()
RefTk.set("Bueno")
FortTk = tk.StringVar()
FortTk.set("Bueno")
VolTk = tk.StringVar()
VolTk.set("Bueno")

RangosTk = tk.StringVar()
TextoRangos = tk.Label(principal, text="Rangos").grid(row=5, column=3)
EntradaRangos = ttk.Entry(principal)
EntradaRangos.grid(row=6, column=3)

VidaTk = tk.StringVar()
TextoVida = tk.Label(principal, text="Vida").grid(row=5, column=4)
EntradaVida = ttk.Entry(principal)
EntradaVida.grid(row=6, column=4)

CATk = tk.StringVar()
CAToqTk = tk.StringVar()
CADesTk = tk.StringVar()

VelTk = tk.StringVar()
TextoVel = tk.Label(principal, text="Velocidad").grid(row=5, column=5)
EntradaVel = ttk.Entry(principal)
EntradaVel.grid(row=6, column=5)

DadoGolpeTk = tk.StringVar()
TextoDadoGolpe = tk.Label(principal, text="Dado de Golpe").grid(row=5, column=6)
EntradaDadoGolpe = ttk.Entry(principal)
EntradaDadoGolpe.grid(row=6, column=6)

BotonTk = tk.Button(text="EL BOTÓN", command=boton).grid(row=8, column=5)

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

# PREPARASIÓN ACABÁ
