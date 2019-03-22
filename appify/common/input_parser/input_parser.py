"""

"""

from abc import ABCMeta, abstractmethod


class InputParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, string):
        """
        Parse the string into the specialized type
        :param string: str to parse
        :type string: str
        :return: True, Value if successful otherwise False, Error message
        """
        pass

    @abstractmethod
    def get_value_format(self):
        """
        :return: A string explaining the expected format of the string to be parsed
        """
        pass


class StrInputParser(InputParser):
    def parse(self, string):
        return True, string

    def get_value_format(self):
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
            return False, "Could not convert {0} into int".format(string)

        return True, val

    def get_value_format(self):
        return "int: 1234 for decimal, 0b0101 for binary, 0xCAFE for hexadecimal"


class FloatInputParser(InputParser):
    def parse(self, string):
        try:
            val = float(string)
        except ValueError:
            return False, "Could not convert {0} into float".format(string)

        return True, val

    def get_value_format(self):
        return "float: 12.4"


class BoolInputParser(InputParser):
    def parse(self, string):
        string = string.strip().lower()
        if string == "0":
            return True, False
        if string == "false":
            return True, False
        if string == "1":
            return True, True
        if string == "true":
            return True, True
        return False, "Could not convert {0} into bool".format(string)

    def get_value_format(self):
        return "bool accepted values: true, false, 0, 1"


