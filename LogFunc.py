from abc import ABC, abstractmethod

# Verwaltungsinfos
__version__ = "3.1" 
__author__ = "Ruben Marcinkowski"


class LogFunc(ABC):
    """The parent class for logic gate classes."""    
    def __init__(self, numInputs = 2):
        """Create a logic gate.
        
        Keyword argument:
        numInputs -- variable number of inputs (two inputs by default). 
        
        Inputs and output get boolean value false by default. 
        """
        self.__Inputs = [False for i in range(numInputs)]
        self.__Output = False
        self.__Name = type(self).__name__
        self.execute()

    # getter and setter
    def __getInputs(self):
        return self.__Inputs

    def __setInputs(self, value):
        self.__Inputs = value

    def __getOutput(self):
        return self.__Output

    def _setOutput(self, output):       # setOutput is protected
        self.__Output = output

    def __getName(self):
        return self.__Name

    def __setName(self, name):
        self.__Name = name

    # methods
    def show(self):
        """print an overview of all inputs and their effect on the output."""
        print(self.__str__())

    def __str__(self):
        self.execute()
        returnString = "Input0(" + str(self.Inputs[0]) + ") "
        for i in range(1, len(self.Inputs)):
            returnString += "und Input" + str(i) + "(" + str(self.Inputs[i]) + ") "
        returnString += "im " + self.Name + " ergibt: " + str(self.Output)
        return returnString

    @abstractmethod
    def execute(self):
        pass

    # properties
    Name = property(__getName, __setName)
    Inputs = property(__getInputs, __setInputs)
    Output = property(__getOutput, None)


class AndGate(LogFunc):
    def execute(self):
        """set the output to true when all inputs are true."""
        if self.Inputs.count(False) == 0:
            self._setOutput(True)
        else:
            self._setOutput(False)


class OrGate(LogFunc):
    def execute(self):
        """set the output to false when all inputs are false."""
        if self.Inputs.count(True) == 0:
            self._setOutput(False)
        else:
            self._setOutput(True)


class XorGate(LogFunc):
    def execute(self):
        """set the output to true when exactly one input is true."""
        if self.Inputs.count(True) == 1:
            self._setOutput(True)
        else:
            self._setOutput(False)


class NandGate(LogFunc):
    def execute(self):
        """set the output to false when all inputs are true."""
        if self.Inputs.count(False) == 0:
            self._setOutput(False)
        else:
            self._setOutput(True)
