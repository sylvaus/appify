from appify.common.exceptions import IncompatibleParameter


class NoDefaultType(object):
    pass


NoDefault = NoDefaultType()


class ParameterInfo(object):
    __slots__ = ["name", "type", "default", "description", "required"]

    def __init__(
        self, name, type_=None, default=NoDefault, description=None, required=False
    ):
        self.name = name
        self.type = type_
        self.default = default
        self.description = description
        self.required = required

    def __repr__(self):
        if self.required:
            string = "Required parameter {0}".format(self.name)
        else:
            string = "Parameter {0}".format(self.name)
        if self.type:
            string += " of type {0}".format(self.type)
        if self.default != NoDefault:
            string += " with default {0}".format(self.default)
        if self.description:
            string += " with description {0}".format(self.description)

        return string

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        if type(other) != ParameterInfo:
            return False
        return (
            (self.name == other.name)
            and (self.type == other.type)
            and (self.default == other.default)
            and (self.description == other.description)
            and (self.required == other.required)
        )

    def is_positional(self):
        """
        :return: If the parameter is positional
        :rtype: bool
        """
        return self.default == NoDefault

    def is_keyword(self):
        """
        :return: If the parameter is keyword
        :rtype: bool
        """
        return self.default != NoDefault

    def update(self, other):
        """
        Update the parameter info with the given other parameter info

        :param other: the ParameterInfo to merge into this one
        :raise: IncompatibleParameter if the two ParameterInfos have incompatible information
        :return: None
        """
        if self.name != other.name:
            raise IncompatibleParameter(
                "Cannot merge two parameters with different names: {0} and {1}".format(
                    self.name, other.name
                )
            )
        if not self._has_compatible_type(self.type, other.type):
            raise IncompatibleParameter(
                "Parameter {0} has two different type defined: {1} and {2}".format(
                    self.name, self.type, other.type
                )
            )
        if not self._has_compatible_default(self.default, other.default):
            raise IncompatibleParameter(
                "Parameter {0} has two different default value defined: {1} and {2}".format(
                    self.name, self.default, other.default
                )
            )
        if not self._has_compatible_description(self.description, other.description):
            raise IncompatibleParameter(
                "Parameter {0} has two different description defined: {1} and {2}".format(
                    self.name, self.description, other.description
                )
            )

        if other.type:
            self.type = other.type
        if other.description:
            self.description = other.description
        if other.default != NoDefault:
            self.default = other.default
        self.required = self.required or other.required

    @staticmethod
    def _has_compatible_type(type_, other_type):
        return (type_ is None) or (other_type is None) or (type_ == other_type)

    @staticmethod
    def _has_compatible_default(default, other_default):
        return (
            (default is NoDefault)
            or (other_default is NoDefault)
            or (default == other_default)
        )

    @staticmethod
    def _has_compatible_description(description, other_description) -> bool:
        return (
            (description is None)
            or (other_description is None)
            or (description == other_description)
        )
