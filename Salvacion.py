class Salvacion:

# Valores base generales de salvaciones "__" indica los valores con cálculos

    __salvacionBase = 0  # Esto dependerá del nivel
    __bonusCaract = 0  # Esto dependerá de una cierta característica, dependiendo de si es Ref(DES), For(CON) o Vol(SAB)
    bonusExtra = 0
    bonusTemp = 0
    __caractTotal = __salvacionBase + __bonusCaract + bonusExtra + bonusTemp

# Funciones de la clase

    def __init__(self, name):
        self.name = name

    def __del__(self):
        pass

    # Setters de valores

    def setsalvacionBase(self, bonus):
        self.__salvacionBase = bonus
        self.__caractTotal = self.__salvacionBase + self.__bonusCaract + self.bonusExtra + self.bonusTemp

    def setbonusCaract(self, bonus):
        self.__bonusCaract = bonus
        self.__caractTotal = self.__salvacionBase + self.__bonusCaract + self.bonusExtra + self.bonusTemp

    def setbonusExtra(self, bonus):
        self.bonusExtra = bonus
        self.__caractTotal = self.__salvacionBase + self.__bonusCaract + self.bonusExtra + self.bonusTemp

    def setbonusTemp(self, bonus):
        self.bonusTemp = bonus
        self.__caractTotal = self.__salvacionBase + self.__bonusCaract + self.bonusExtra + self.bonusTemp

    # Getters de valores

    def getsalvacionBase(self):
        return self.__salvacionBase

    def getbonusCaract(self):
        return self.__bonusCaract

    def getbonusExtra(self):
        return self.bonusExtra

    def getbonusTemp(self):
        return self.bonusTemp

    def getcaractTotal(self):
        print(self.__caractTotal)
