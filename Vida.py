class Vida:

# Valores base generales de vida "__" indica los valores con cálculos

    bonusCon = 0
    __vidaTotal = bonusCon
    pg = []
    for i in range(20):
        pg.append(0)

    for i in pg:
        __vidaTotal += i

# Funciones de la clase

    def __init__(self):
        pass

    def __del__(self):
        pass

    # Setters de valores

    def setpg(self, lvl, bonus):
        self.pg[lvl-1] = bonus
        self.__vidaTotal = self.bonusCon
        for i in self.pg:
            self.__vidaTotal += i

    def setbonusCon(self, bonus):
        self.__vidaTotal -= self.bonusCon
        self.bonusCon = bonus
        self.__vidaTotal += self.bonusCon

    # Getters de valores

    def getpg(self, lvl):
        return self.pg[lvl-1]

    def getbonusCon(self):
        return self.bonusCon

    def getvidaTotal(self):
        return self.__vidaTotal
