from abc import ABC, abstractmethod

__version__ = "4.0"  # Verwaltungsinfos
__author__ = "Ruben Marcinkowski"


class LogFunc(ABC):
    """The parent class for logic gate classes."""
    def __init__(self, numInputs, numOutputs):
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
    def __init__(self, numInputs = 2):        
        super().__init__(numInputs,1)

    def execute(self):
        """set the outputs to true when all inputs are true."""
        if self.Inputs.count(False) == 0:
            self._setOutputs(True)
        else:
            self._setOutputs(False)


class OrGate(LogFunc):
    def __init__(self, numInputs = 2):        
        super().__init__(numInputs,1)

    def execute(self):
        """set the outputs to false when all inputs are false."""
        if self.Inputs.count(True) == 0:
            self._setOutputs(False)
        else:
            self._setOutputs(True)


class XorGate(LogFunc):
    def __init__(self, numInputs = 2):        
        super().__init__(numInputs,1)

    def execute(self):
        """set the outputs to true when exactly one input is true."""
        if self.Inputs.count(True) % 2 == 1:
            self._setOutputs(True)
        else:
            self._setOutputs(False)


class NandGate(LogFunc):
    def __init__(self, numInputs = 2):        
        super().__init__(numInputs,1)

    def execute(self):
        """set the outputs to false when all inputs are true."""
        if self.Inputs.count(False) == 0:
            self._setOutputs(False)
        else:
            self._setOutputs(True)

class NotGate(LogFunc):
    def __init__(self, numInputs = 2):        
        super().__init__(numInputs, numInputs)
        
    def execute(self):
        """set the output at the specific index to the opposite of the input at that position."""
        outputs = [None] * len(self.Outputs)
        for i in range(len(self.Inputs)):
            outputs[i] = not self.Inputs[i]
        self._setOutputs(outputs)
