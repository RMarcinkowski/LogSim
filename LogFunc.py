from abc import ABC, abstractmethod

__version__ = "3.2"  # Verwaltungsinfos
__author__ = "Ruben Marcinkowski"


class LogFunc(ABC):
    """The parent class for logic gate classes."""
    def __init__(self, numInputs = 2, numOutputs = 1):
        """Create a logic gate.

        Keyword argument:
        numInputs -- variable number of inputs (two inputs by default).
        numOutputs -- variable number of outputs (one output by default).

        Inputs and output get boolean value false by default.
        """
        self.__Inputs = [False] * numInputs
        self.__Outputs = [False] * numOutputs
        self.__Name = type(self).__name__
        self.execute()

    # getter and setter
    def __getInputs(self):
        return self.__Inputs

    def __setInputs(self, inputs):
        self.__Inputs = inputs

    def __getOutputs(self):
        return self.__Outputs

    def _setOutputs(self, outputs):       # setOutputs is protected
        self.__Outputs = outputs

    def __getName(self):
        return self.__Name

    def __setName(self, name):
        self.__Name = name

    # methods
    def show(self):
        """print an overview of all inputs and their effect on the outputs."""
        print(self.__str__())

    def __str__(self):
        self.execute()
        ausgangsstring = "einem Ausgang"
        if len(self.Outputs) > 1:
            ausgangsstring = str(len(self.Outputs)) + " Ausgängen"
        return "Die Eingänge " + str(self.Inputs) + " ergeben im " \
               + self.Name + " mit " + ausgangsstring + " folgende Werte: " + str(self.Outputs)

    @abstractmethod
    def execute(self):
        pass

    # properties
    Name = property(__getName, __setName)
    Inputs = property(__getInputs, __setInputs)
    Outputs = property(__getOutputs, None)


class AndGate(LogFunc):
    def execute(self):
        """set the outputs to true when all inputs are true."""
        if self.Inputs.count(False) == 0:
            self._setOutputs([True] * len(self.Outputs))
        else:
            self._setOutputs([False] * len(self.Outputs))


class OrGate(LogFunc):
    def execute(self):
        """set the outputs to false when all inputs are false."""
        if self.Inputs.count(True) == 0:
            self._setOutputs([False] * len(self.Outputs))
        else:
            self._setOutputs([True] * len(self.Outputs))


class XorGate(LogFunc):
    def execute(self):
        """set the outputs to true when exactly one input is true."""
        if self.Inputs.count(True) == 1:
            self._setOutputs([True] * len(self.Outputs))
        else:
            self._setOutputs([False] * len(self.Outputs))


class NandGate(LogFunc):
    def execute(self):
        """set the outputs to false when all inputs are true."""
        if self.Inputs.count(False) == 0:
            self._setOutputs([False] * len(self.Outputs))
        else:
            self._setOutputs([True] * len(self.Outputs))

class NotGate(LogFunc):
    def execute(self):

        if len(self.Inputs) != len(self.Outputs):
            raise ArithmeticError("The number of inputs has to be equal to the number of outputs!")
        outputs = [None] * len(self.Outputs)
        for i in range(len(self.Inputs)):
            outputs[i] = not self.Inputs[i]
        self._setOutputs(outputs)
