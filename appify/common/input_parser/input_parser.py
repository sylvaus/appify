"""

"""

from abc import ABCMeta, abstractmethod
from argparse import ArgumentTypeError


class InputParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, string):
        """
        Parse the string into the specialized type
        :param string: str to parse
        :type string: str
        :return: Value if successful otherwise raise ArgumentTypeError
        """
        pass

    @property
    @abstractmethod
    def value_format(self):
        """
        :return: A string explaining the expected format of the string to be parsed
        """
        pass


class StrInputParser(InputParser):
    def parse(self, string):
        return string

    def value_format(self):
        return "string: text"


class IntInputParser(InputParser):
    def parse(self, string):
        string = string.strip()
        int_format = 10
        if string.startswith("0b"):
            int_format = 2
        elif string.startswith("0x"):
            int_format = 16
        try:
            val = int(string, int_format)
        except ValueError:
            pass  # Avoid Exception chaining
        else:
            return val

        raise ArgumentTypeError("Could not convert \"{0}\" into int".format(string))

    @property
    def value_format(self):
        return "int: 1234 for decimal, 0b0101 for binary, 0xCAFE for hexadecimal"


class FloatInputParser(InputParser):
    def parse(self, string):
        try:
            val = float(string)
        except ValueError:
            pass  # Avoid Exception chaining
        else:
            return val

        raise ArgumentTypeError("Could not convert \"{0}\" into float".format(string))

    @property
    def value_format(self):
        return "float: 12.4"


class BoolInputParser(InputParser):
    def parse(self, string):
        string = string.strip().lower()
        if string.lower() == "0":
            return False
        if string.lower() == "false":
            return False
        if string.lower() == "1":
            return True
        if string.lower() == "true":
            return True
        raise ArgumentTypeError("Could not convert \"{0}\" into bool".format(string))

    @property
    def value_format(self):
        return "bool accepted values: true, false, 0, 1"
