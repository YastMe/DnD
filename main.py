import tkinter as tk
# import math
from tkinter import ttk
import os


# DEBUG:

def gestionar_pulsacion_raton(event):
    print("Se ha pulsado el ratón en la posición x: {} y:{}".format(event.x, event.y))


def winconfig(ventana, nombre, dimensiones, resize):
    ventana.title(nombre)
    ventana.geometry(dimensiones)
    ventana.resizable(width=resize, height=resize)
    ventana.configure(background='lightgrey')
    ventana.bind("<Button-1>", gestionar_pulsacion_raton)


def botonAceptar():
    global ListaTk

    f_list = os.listdir("./")

    if "Jugador.txt" in f_list:
        e = open("Jugador.txt", "w", encoding="utf-8")
    else:
        e = open("Jugador.txt", "w", encoding="utf-8")

    e.write("%s\n" % DadoGolpeTk.get())

    for c in range(0, len(ListaTk)):
        if (c % 2) == 0:
            ListaTk[c].set(ListaTk[c + 1].get())
            e.write(ListaTk[c].get() + "\n")

    e.close()

    rangFile = open("Rangos.txt", "w", encoding="utf-8")

    for n in range(0, 47):
        if ListaRangosAsignados[n].get():
            ListaRangos[n].append(True)
        else:
            ListaRangos[n].append(False)
        ListaRangos[n][3] = 0
        rangFile.writelines(
            ListaRangos[n][0] + ',' + ListaRangos[n][1] + ',' + ListaRangos[n][2] + ',' + str(ListaRangos[n][3]) + ',' +
            str(ListaRangos[n][4]) + "\n")

    rangFile.close()
    principal.destroy()
    # open("Abrido.txt", "w", encoding="utf-8").write("1")


def botonCancelar():
    comprobacion.destroy()


def boton():
    global comprobacion

    comprobacion = tk.Toplevel(principal)
    comprobacion.transient(principal)
    comprobacion.title(" ")
    comprobacion.geometry("250x60+300+200")
    comprobacion.resizable(width="False", height="False")

    tk.Label(comprobacion, text="¿Segure que quieres guardar los cambios así?").pack(side="top")
    tk.Button(comprobacion, text="Sí", command=botonAceptar).place(x=25, y=30, width=95)
    tk.Button(comprobacion, text="No", command=botonCancelar).place(x=130, y=30, width=95)


def scroll(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def callback(selection):
    global DadoGolpeTk
    print(selection)
    DadoGolpeTk.set(selection)
    print(DadoGolpeTk.get())


Abrido = open("Abrido.txt", "r", encoding="utf-8")

if Abrido.readline() == "0":
    Abrido.close()

    principal = tk.Tk()
    winconfig(principal, nombre="Ficha Python", dimensiones="860x345+200+100", resize="False")
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
    TextoAlineamiento = tk.Label(principal, text="Alineamiento", anchor='w', relief="groove").place(x=420, y=91,
                                                                                                    width=100)
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
    TextoEXPH = tk.Label(principal, text="EXPH", anchor='w', relief="groove")  # .place(x=10, y=211, width=50)
    EntradaEXPH = ttk.Entry(principal)
    # EntradaEXPH.place(x=10, y=190, width=50)

    VidaTk = tk.StringVar()
    TextoVida = tk.Label(principal, text="Vida", anchor='w', relief="groove").place(x=10, y=211, width=145)
    EntradaVida = ttk.Entry(principal)
    EntradaVida.place(x=10, y=190, width=145)

    RangosTk = tk.StringVar()
    TextoRangos = tk.Label(principal, text="Rangos", anchor='w', relief="groove").place(x=165, y=211, width=145)
    EntradaRangos = ttk.Entry(principal)
    EntradaRangos.place(x=165, y=190, width=145)

    VelTk = tk.StringVar()
    TextoVel = tk.Label(principal, text="Velocidad", anchor='w', relief="groove").place(x=320, y=211, width=145)
    EntradaVel = ttk.Entry(principal)
    EntradaVel.place(x=320, y=190, width=145)

    DadoGolpeTk = tk.StringVar()
    TextoDadoGolpe = tk.Label(principal, text="Dado de Golpe", anchor='w', relief="groove").place(x=475, y=211,
                                                                                                  width=145)
    EntradaDadoGolpe = ttk.Entry(principal)
    # EntradaDadoGolpe.place(x=475, y=190, width=145)

    ListaDados = []
    DadoGolpeTk.set("1d4")
    opt = tk.OptionMenu(principal, DadoGolpeTk, "1d4", "1d6", "1d8", "1d10", "1d12", command=callback)
    opt.configure(width=145)
    opt.place(x=475, y=190, width=145)

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
    CATk = tk.StringVar()
    CAToqTk = tk.StringVar()
    CADesTk = tk.StringVar()

    ListaTk = [NombreTk, EntradaNombre, JugadorTk, EntradaJugador, ClaseTk, EntradaClase, Lv, EntradaLv, RazaTk,
               EntradaRaza, AlineamientoTk, EntradaAlineamiento, DeidadTk, EntradaDeidad, TamanioTk, EntradaTamanio,
               EdadTk, EntradaEdad, SexoTk, EntradaSexo, AlturaTk, EntradaAltura, PesoTk, EntradaPeso, OjosTk,
               EntradaOjos, CabelloTk, EntradaCabello, PielTk, EntradaPiel, VidaTk, EntradaVida, RangosTk,
               EntradaRangos, VelTk, EntradaVel, CobreTk, EntradaCobre, PlataTk,
               EntradaPlata, OroTk, EntradaOro, PlatinoTk, EntradaPlatino]

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

    BotonTk = tk.Button(principal, text="Guardar los cambios", command=boton).place(x=370, y=310)

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

    # f = open("Abrido.txt", "w", encoding="utf-8")
    # f.write("1")
    # f.close()

    # PREPARASIÓN ACABÁ

#############################################################################

# Aquí comiensa la programasión del de verdá

# fichaWin = tk.Tk()
# winconfig(fichaWin, nombre="Ficha 3.5", dimensiones="1280x720+200+100", resize="True")
#
# StatsFile = open("Jugador.txt", "r", encoding="utf-8")
#
# StatsFile.close()
#
# NombreEntry = tk.Entry(fichaWin)
# NombreEntry.place(x=10, y=10, width=100)
# NombreEntry.set(ListaTk)
# NombreDefLabel = tk.Label(fichaWin, text="Nombre", anchor='w', relief="groove")
# NombreDefLabel.place(x=10, y=31, width=100)
#
# JugadorEntry = tk.Entry(fichaWin)
# NombreEntry.place(x=10, y=10, width=100)
# NombreDefLabel = tk.Label(fichaWin, text="Nombre", anchor='w', relief="groove")
# NombreDefLabel.place(x=10, y=31, width=100)
#
# fichaWin.mainloop()
