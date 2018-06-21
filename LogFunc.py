from abc import ABC, abstractmethod

__version__ = "6.1"  # Verwaltungsinfos
__author__ = "Ruben Marcinkowski"


class LogFunc(ABC):
    """The parent class for logic gate classes."""

    def __init__(self, numInputs, numOutputs):
        """Create a logic gate.

        Keyword argument:
        numInputs -- variable number of inputs.
        numOutputs -- variable number of outputs.

        Inputs and output get boolean value false by default.
        """
        self.__Inputs = [False] * numInputs
        self.__Outputs = [False] * numOutputs
        self.__Name = type(self).__name__
        self.__ShowBehavior = DefaultShow()
        self._Symbol = ""
        self.execute()

    # getter and setter
    def __getInputs(self):
        return self.__Inputs

    def __setInputs(self, inputs):
        self.__Inputs = inputs

    def __getOutputs(self):
        return self.__Outputs

    def _setOutputs(self, outputs):  # setOutputs is protected
        self.__Outputs = outputs

    def __getName(self):
        return self.__Name

    def __setName(self, name):
        self.__Name = name

    def setShow(self, showBehavior):
        self.__ShowBehavior = showBehavior

    # methods
    def show(self):
        """Print an overview of all inputs and their effect on the outputs."""
        self.__str__()

    def __str__(self):
        self.execute()
        self.__ShowBehavior.show(self)

    @abstractmethod
    def execute(self):
        pass

    # properties
    Name = property(__getName, __setName)
    Inputs = property(__getInputs, __setInputs)
    Outputs = property(__getOutputs, None)


class AndGate(LogFunc):
    def __init__(self, numInputs=2):
        """Set the number of inputs (default: 2) and one output."""
        super().__init__(numInputs, 1)
        self._Symbol = "&"

    def execute(self):
        """Set the outputs to true when all inputs are true."""
        if self.Inputs.count(False) == 0:
            self._setOutputs(True)
        else:
            self._setOutputs(False)


class OrGate(LogFunc):
    def __init__(self, numInputs=2):
        """Set the number of inputs (default: 2) and one output."""
        super().__init__(numInputs, 1)
        self._Symbol = "≥1"

    def execute(self):
        """Set the outputs to false when all inputs are false."""
        if self.Inputs.count(True) == 0:
            self._setOutputs(False)
        else:
            self._setOutputs(True)


class XorGate(LogFunc):
    def __init__(self, numInputs=2):
        """Set the number of inputs (default: 2) and one output."""
        super().__init__(numInputs, 1)
        self._Symbol = "=1"

    def execute(self):
        """Set the outputs to true when the number of true inputs is even."""
        if self.Inputs.count(True) % 2 == 1:
            self._setOutputs(True)
        else:
            self._setOutputs(False)


class NandGate(LogFunc):
    def __init__(self, numInputs=2):
        """Set the number of inputs (default: 2) and one output."""
        super().__init__(numInputs, 1)
        self._Symbol = "!&"

    def execute(self):
        """Set the outputs to false when all inputs are true."""
        if self.Inputs.count(False) == 0:
            self._setOutputs(False)
        else:
            self._setOutputs(True)


class NotGate(LogFunc):
    def __init__(self, numInputs=2):
        """Set the number of inputs and outputs (default: 2)."""
        super().__init__(numInputs, numInputs)
        self._Symbol = "!1"

    def execute(self):
        """Set the output at the specific index to the opposite of the input at that position."""
        outputs = [False] * len(self.Outputs)
        for i in range(len(self.Inputs)):
            outputs[i] = not self.Inputs[i]
        self._setOutputs(outputs)


class HalfAdder(LogFunc):
    def __init__(self):
        """Set 2 inputs and 2 outputs."""
        self.__sum = XorGate(2)
        self.__carry = AndGate(2)
        super().__init__(2, 2)
        self.setShow(HalfAdderShow())

    def execute(self):
        """Set the outputs to carry and sum of the half adder."""
        self.__sum.Inputs = self.Inputs
        self.__carry.Inputs = self.Inputs
        self.__sum.execute()
        self.__carry.execute()
        self._setOutputs([self.__carry.Outputs, self.__sum.Outputs])


class FullAdder(LogFunc):
    def __init__(self):
        """Set 3 inputs and 2 outputs."""
        self.__sum = [HalfAdder(), HalfAdder()]
        self.__carry = OrGate()
        super().__init__(3, 2)
        self.setShow(FullAdderShow())

    def execute(self):
        """Set the outputs to carry and sum of the full adder."""
        self.__sum[0].Inputs = [self.Inputs[0], self.Inputs[1]]
        self.__sum[0].execute()
        self.__sum[1].Inputs = [self.__sum[0].Outputs[1], self.Inputs[2]]
        self.__sum[1].execute()
        self.__carry.Inputs = [self.__sum[0].Outputs[0], self.__sum[1].Outputs[0]]
        self.__carry.execute()
        self._setOutputs([self.__carry.Outputs, self.__sum[1].Outputs[1]])


class EightBitAdder(LogFunc):
    def __init__(self):
        """Set 16 inputs and 9 outputs.

        The first 8 inputs are for the first number to add,
        9th-16th for the second number.
        """
        self.__adder = [FullAdder()] * 8
        super().__init__(16, 9)
        self.setShow(EightBitShow())

    def execute(self):
        """Add two 8-bit numbers and get a 9-bit sum"""
        carry = 0
        sumOutputs = len(self.Outputs) - 1
        outputs = [None] * (sumOutputs + 1)
        for i in range(sumOutputs):
            self.__adder[i].Inputs = [carry, self.Inputs[i], self.Inputs[i + sumOutputs]]
            self.__adder[i].execute()
            carry = self.__adder[i].Outputs[0]
            outputs[i] = self.__adder[i].Outputs[1]
        outputs[sumOutputs] = carry
        self._setOutputs(outputs)


class ShowBehavior(ABC):
    @abstractmethod
    def show(self, logFunc):
        raise NotImplementedError()

    def _boolToBinary(self, bool_values):
        if isinstance(bool_values, bool):
            if bool_values:
                return "1"
            else:
                return "0"
        for i in range(len(bool_values)):
            if bool_values[i]:
                bool_values[i] = "1"
            else:
                bool_values[i] = "0"
        return bool_values


class DefaultShow(ShowBehavior):
    def show(self, logFunc):
        ausgangsstring = "einem Ausgang"
        if not isinstance(logFunc.Outputs, bool):
            ausgangsstring = str(len(logFunc.Outputs)) + " Ausgängen"
        print("Die Eingänge " + str(logFunc.Inputs) + " ergeben im " \
               + logFunc.Name + " mit " + ausgangsstring + " folgende Werte: " + str(logFunc.Outputs))


class StarGateShow():
    def __init__(self):
        self._cwidth = 54

    def _get_line(self, left_text, right_text):
        return "**" + left_text.ljust(int(self._cwidth / 3 - 2), " ") + "|" + right_text.ljust(
            int((2 * self._cwidth) / 3) - 3, " ") + "**"


class GatterShow(ShowBehavior, StarGateShow):
    def show(self, logFunc):
        inputs = self._boolToBinary(logFunc.Inputs)
        len_inputs = len(inputs)
        outputs = self._boolToBinary(logFunc.Outputs)
        empty_line = self._get_line("", "")
        first_last = "".ljust(self._cwidth, "*")
        mid = self._get_line("_" * (int(self._cwidth / 3) - 2), "_" * (int(2 * self._cwidth / 3) - 3))

        print("\n" + first_last)
        print(self._get_line(" " + logFunc.Name, ""))
        print(self._get_line("", "  Input0 = " + inputs[0]))
        for i in range(1,len_inputs-1):
            print(self._get_line(" " * (int(self._cwidth / 3) - 5), "  Input" + str(i) + " = " + inputs[i]))
        print(self._get_line(" " * (int(self._cwidth / 3) - 5) + logFunc._Symbol, "  Input" + str(len_inputs-1) + " = " + inputs[len_inputs-1]))
        print(mid)
        print(empty_line)
        if len(outputs) == 1:
            print(self._get_line("", "  Output = " + outputs[0]))
        else:
            for i in range(len(outputs)):
                print(self._get_line("", "  Output" + str(i) + " = " + outputs[i]))
        print(empty_line)
        print(first_last + "\n")


class HalfAdderShow(ShowBehavior, StarGateShow):
    def show(self, logFunc):
        inputs = self._boolToBinary(logFunc.Inputs)
        outputs = self._boolToBinary(logFunc.Outputs)
        empty_line = self._get_line("", "")
        first_last = "".ljust(self._cwidth, "*")
        mid = self._get_line("_" * (int(self._cwidth / 3) - 2), "_" * (int(2 * self._cwidth / 3) - 3))

        print("\n" + first_last)
        print(self._get_line(" " + logFunc.Name, ""))
        print(self._get_line("", "  A = " + inputs[0]))
        print(self._get_line(" " * (int(self._cwidth / 3) - 5) + "+", "  B = " + inputs[1]))
        print(mid)
        print(empty_line)
        print(self._get_line("  Carry = " + outputs[0], "  Sum = " + outputs[1]))
        print(empty_line)
        print(first_last + "\n")


class FullAdderShow(ShowBehavior, StarGateShow):
    def show(self, logFunc):
        inputs = self._boolToBinary(logFunc.Inputs)
        outputs = self._boolToBinary(logFunc.Outputs)
        empty_line = self._get_line("", "")
        first_last = "".ljust(self._cwidth, "*")
        mid = self._get_line("_" * (int(self._cwidth / 3) - 2), "_" * (int(2 * self._cwidth / 3) - 3))

        print("\n" + first_last)
        print(self._get_line(" " + logFunc.Name, ""))
        print(self._get_line("", "  Carry in = " + inputs[0]))
        print(self._get_line("", "  A        = " + inputs[1]))
        print(self._get_line(" " * (int(self._cwidth / 3) - 5) + "+", "  B        = " + inputs[2]))
        print(mid)
        print(empty_line)
        print(self._get_line("  Carry out = " + outputs[0], "  Sum = " + outputs[1]))
        print(empty_line)
        print(first_last + "\n")


class EightBitShow(ShowBehavior, StarGateShow):
    def show(self, logFunc):
        inputs = self._boolToBinary(logFunc.Inputs)
        outputs = self._boolToBinary(logFunc.Outputs)
        inputsA = ""
        for i in range(8):
            inputsA += str(inputs[i])
        inputsA = inputsA[::-1]
        inputsB = ""
        for i in range(8, 16):
            inputsB += str(inputs[i])
        inputsB = inputsB[::-1]
        sum_line = ""
        for i in range(8):
            sum_line += str(outputs[i])
        sum_line = sum_line[::-1]
        empty_line = self._get_line("", "")
        first_last = "".ljust(self._cwidth, "*")
        mid = self._get_line("_" * (int(self._cwidth / 3) - 2), "_" * (int(2 * self._cwidth / 3) - 3))

        print("\n" + first_last)
        print(self._get_line(" " + logFunc.Name, ""))
        print(self._get_line("", "  A = " + inputsA))
        print(self._get_line(" " * (int(self._cwidth / 3) - 5) + "+", "  B = " + inputsB))
        print(mid)
        print(empty_line)
        print(self._get_line("  Carry = " + outputs[8], "  Sum = " + sum_line))
        print(empty_line)
        print(first_last + "\n")
