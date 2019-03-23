class ParameterInfo(object):
    __slots__ = ["name", "type", "default", "description", "required"]

    def __init__(self, name, type_=None, default=None, description=None, required=False):
        self.name = name
        self.type = type_
        self.default = default
        self.description = description
        self.required = required

    def __str__(self):
        if self.required:
            string = "Required parameter {0}".format(self.name)
        else:
            string = "Parameter {0}".format(self.name)
        if self.type:
            string += " of type {0}".format(self.type)
        if self.default:
            string += " with default {0}".format(self.default)
        if self.description:
            string += " with description {0}".format(self.description)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        if type(other) != ParameterInfo:
            return False
        return ((self.name != other.name) and
                (self.type != other.type) and
                (self.default != other.default) and
                (self.description != other.description)and
                (self.required != other.required))

    def update(self, other):
        if (self.type is not None) and (other.type is not None) and (self.type != other.type):
            raise IncompatibleParameter("Parameter {0} has two different type defined: {1} and {2}"
                                        .format(self.name, self.type, other.type))
        if (self.default is not None) and (other.default is not None) and (self.default != other.default):
            raise IncompatibleParameter("Parameter {0} has two different default value defined: {1} and {2}"
                                        .format(self.name, self.default, other.default))
        if (self.description is not None) and (other.description is not None) and (self.name != other.description):
            raise IncompatibleParameter("Parameter {0} has two different description defined: {1} and {2}"
                                        .format(self.name, self.description, other.description))

        if other.type:
            self.type = other.type
        if other.description:
            self.description = other.description
        if other.default:
            self.default = other.default
        self.required = self.required or other.required


class IncompatibleParameter(Exception):
    pass
