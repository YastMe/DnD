class Arma:

# Valores base generales de armas "__" indica los valores con cálculos

    caract = ""
    bonusAt = 0
    bonusDam = 0
    damageDice = ""
    damagePlus = 0
    critico = ""
    alcance = ""
    tipo = ""
    mano = ""
    notas = ""

# Funciones de la clase

    def __init__(self, name):
        self.name = name

    def __del__(self):
        pass

    # Setters de valores

    def setcaract(self, atributo):
        self.caract = atributo

    def setbonusAt(self, bonus):
        self.bonusAt = bonus

    def setbonusDam(self, bonus):
        self.bonusDam = bonus

    def setdamageDice(self, dice):
        self.damageDice = dice

    def setdamagePlus(self, bonus):
        self.damagePlus = bonus

    def setcritico(self, crit):
        self.critico = crit

    def setalcance(self, reach):
        self.alcance = reach

    def settipo(self, type):
        self.tipo = type

    def setmano(self, hand):
        self.mano = hand

    def setnotas(self, text):
        self.notas = text

    # Getters de valores


    def getcaract(self):
        return self.caract


    def getbonusAt(self):
        return self.bonusAt


    def getbonusDam(self):
        return self.bonusDam


    def getdamageDice(self):
        return self.damageDice


    def getdamagePlus(self):
        return self.damagePlus


    def getcritico(self):
        return self.critico


    def getalcance(self):
        return self.alcance


    def gettipo(self):
        return self.tipo


    def getmano(self):
        return self.mano


    def getnotas(self):
        return self.notas