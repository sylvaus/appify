from appify.exceptions import AppifyException


class InvalidArgument(AppifyException):
    pass


class UnknownTypeArgument(AppifyException):
    pass


class ParameterParsingException(AppifyException):
    pass


class IncompatibleParameter(ParameterParsingException):
    pass
