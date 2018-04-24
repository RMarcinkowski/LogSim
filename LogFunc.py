__version__ = "2"                             # Verwaltungsinfos
__author__ = "Ruben Marcinkowski"

class LogFunc:
    def __init__(self):
        self.__Input0 = False
        self.__Input1 = False
        self._Output = False            # Output is protected
        self.__Name = ""

    # getter and setter
    def __getInput0(self):
        return self.__Input0

    def __setInput0(self, input):
        self.__Input0 = input

    def __getInput1(self):
        return self.__Input1

    def __setInput1(self, input):
        self.__Input1 = input

    def __getOutput(self):
        return self._Output

    def __getName(self):
        return self.__Name

    def __setName(self, name):
        self.__Name = name

    # methods
    def show(self):
        print(self.__str__())

    def __str__(self):
        return "Input0(" + str(self.Input0) + ") und Input1(" + str(self.Input1) + ") ergibt: " + str(self.Output)

    # properties
    Name = property(__getName, __setName)
    Input0 = property(__getInput0, __setInput0)
    Input1 = property(__getInput1, __setInput1)
    Output = property(__getOutput, None)


class AndGate(LogFunc):
    def execute(self):
        if self.Input0 == self.Input1 == True:
            self._Output = True
        else:
            self._Output = False

class OrGate(LogFunc):    
    def execute(self):
        if self.Input0 == self.Input1 == False:
            self._Output = False
        else:
            self._Output = True

class XorGate(LogFunc):
    def execute(self):
        if self.Input0 == self.Input1:
            self._Output = False
        else:
            self._Output = True
