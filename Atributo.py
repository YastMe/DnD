class Atributo:

# Valores base generales de atributos "__" indica los valores con cálculos

    caractBase = 10
    bonusExtra = 0
    bonusTemp = 0
    __caractTotal = caractBase + bonusExtra + bonusTemp
    __modificador = (__caractTotal - 10) / 2

# Funciones de la clase

    def __init__(self, name):
        self.name = name

    def __del__(self):
        pass

    # Setters de valores

    def setcaractBase(self, bonus):
        self.caractBase = bonus
        self.__caractTotal = self.caractBase + self.bonusExtra + self.bonusTemp
        self.__modificador = (self.__caractTotal - 10) / 2

    def setbonusExtra(self, bonus):
        self.bonusExtra = bonus
        self.__caractTotal = self.caractBase + self.bonusExtra + self.bonusTemp
        self.__modificador = (self.__caractTotal - 10) / 2

    def setbonusTemp(self, bonus):
        self.bonusTemp = bonus
        self.__caractTotal = self.caractBase + self.bonusExtra + self.bonusTemp
        self.__modificador = (self.__caractTotal - 10) / 2

    # Getters de valores

    def getcaractBase(self):
        return self.caractBase

    def getbonusExtra(self):
        return self.bonusExtra

    def getbonusTemp(self):
        return self.bonusTemp

    def getcaractTotal(self):
        return self.__caractTotal

    def getmodificador(self):
        return self.__modificador
