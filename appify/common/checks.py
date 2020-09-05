from appify.common.exceptions import InvalidArgument
from appify.common.parameter_info import NoDefault


def check_parameter_info(parameter_info, accepted_types=None):
    """
    Check if the parameter info describe a valid parameter
    Checks are:
        - A parameter cannot be not required and without a default
        - A parameter should have a type
        - The type should be a know type, i.e, is a key of the input_parsers dictionary
        - As one of the accepted types if a list is given

    :param parameter_info: ParameterInfo to check
    :param accepted_types: List of parameter types that should be considered valid
        if None is given (default) all types are accepted
    :raises: InvalidArgument if any of the check fails
    """
    if not parameter_info.required and parameter_info.default == NoDefault:
        raise InvalidArgument(
            "Parameter {0} is not required but does not have a default value\n"
            "Either add a default value or make the parameter".format(
                parameter_info.name
            )
        )

    if not parameter_info.type:
        raise InvalidArgument(
            "Parameter {0} must have a type".format(parameter_info.name)
        )

    if parameter_info.type not in accepted_types:
        raise InvalidArgument(
            "Parameter {0} has an unknown type: {1}. Know types are {2}.".format(
                parameter_info.name, parameter_info.type, ", ".join(accepted_types)
            )
        )
