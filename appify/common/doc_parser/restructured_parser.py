import re
from collections import OrderedDict

from appify.common.doc_parser.doc_parser import DocParser
from appify.common.parameter_info import ParameterInfo


def count_leading_space(line):
    return len(line) - len(line.lstrip())


class RestructuredParser(DocParser):
    NAME = "name"
    DESCRIPTION = "description"
    TYPE_INFO = "info_type"
    TYPE_INFO_DESCRIPTION = "param"
    TYPE_INFO_TYPE = "type"
    REGEX = r"\s*:\s*(?P<info_type>[a-zA-Z0-9-_]+)+\s*(?P<name>[a-zA-Z0-9-_]+)\s*:\s*(?P<description>.*)"

    def __init__(self):
        self._regex = re.compile(self.REGEX)

    def parse(self, docstring):
        """
        Parse the docstring
        :param docstring:
            docstring to parse
        :return: Dictionary of ParameterInfo with the name as key
        """
        lines = [line for line in docstring.split("\n") if line.strip() != ""]

        result = OrderedDict()
        length = len(lines)
        index = 0
        while index < length:
            match = self._regex.match(lines[index])
            if match is None:
                index += 1
                continue

            name = match.group(self.NAME)
            text = match.group(self.DESCRIPTION)
            type_info = match.group(self.TYPE_INFO)
            index, additional_text = self._get_info_text(lines, index, length)
            text += additional_text

            if type_info == self.TYPE_INFO_DESCRIPTION:
                if name not in result:
                    result[name] = ParameterInfo(name)
                result[name].description = text

            if type_info == self.TYPE_INFO_TYPE:
                if name not in result:
                    result[name] = ParameterInfo(name)
                result[name].type = text

        return result

    @staticmethod
    def _get_info_text(lines, index, length):
        """
        Collect all the lines related to the one defined by the index given
        :param lines:
            docstring lines
        :param index:
            index of the beginning of the parameter info
        :param length:
            length of the docstring
        :return: index of the next unprocessed line, text associated
        """
        initial_indent = count_leading_space(lines[index])
        text = ""

        index += 1
        while (index < length) and (count_leading_space(lines[index]) > initial_indent):
            text += (" " + lines[index].trim())
            index += 1

        return index, text
