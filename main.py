import tkinter as tk
import math

def winconfig():
    principal.title("Ficha Python")
    principal.geometry("1280x720+200+100")
    principal.resizable(width="True", height="True")


principal = tk.Tk()
winconfig()

StatsBase = []
StatsTotal = []
DadosVida = []

ClaseTk = tk.StringVar()
Lv = tk.IntVar()
Lv.set(3)
BaBTk = tk.StringVar()
BaBTk.set("Malo")
RefTk = tk.StringVar()
RefTk.set("Bueno")
FortTk = tk.StringVar()
FortTk.set("Bueno")
VolTk = tk.StringVar()
VolTk.set("Bueno")
Rangos = tk.IntVar()
VidaTk = tk.IntVar()
CATk = tk.IntVar()
CAToqTk = tk.IntVar()
CADesTk = tk.IntVar()
VelTk = tk.IntVar()

DadoGolpe = int(input("TU VIDA"))

for i in range(0,6):
    StatsBase.append(int(input("Inserta estadística ")))
    StatsTotal.append(math.floor((StatsBase[i]-10)/2))

VidaTotal = DadoGolpe + StatsTotal[2]
Iniciativa = StatsTotal[1]
CA = 10+StatsTotal[1]
CAToq = 10+StatsTotal[1]
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

for i in range(0,Lv.get()-1):
    VidaTotal = VidaTotal + int(input()) + StatsTotal[2]

if BaBTk.get() == "Bueno":
    BaB = Lv.get()
elif BaBTk.get() == "Regular":
    BaB = Lv.get()-math.ceil(Lv.get()/4)
else:
    BaB = int(Lv.get()/2)

print(BaB)
print(VidaTotal)
print(StatsBase)
print(StatsTotal)

# principal.mainloop()
