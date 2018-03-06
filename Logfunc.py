__version__ = "1.0"                             #Verwaltungsinfos
__author__ = "Ruben Marcinkowski"

class AndGate:                                  #Klassendefinition
    def __init__(self):                         #Attribute definieren
        self.Input0 = False
        self.Input1 = False
        self.Output = False
        self.Name = "YaAndGate"

    def show(self):
        print(self.__str__())

    def execute(self):
        if self.Input0 == self.Input1 == True:
            self.Output = True
        else:
            self.Output = False

    def __str__(self):
        return "Input0(" + str(self.Input0) + ") und Input1(" + str(self.Input1) + ") ergibt: " + str(self.Output)



AND = AndGate()
AND.Input0 = True
AND.execute()
AND.show()
AND.Input1 = True
AND.execute()
AND.show()
