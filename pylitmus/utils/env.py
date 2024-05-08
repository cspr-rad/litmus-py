import os
import typing

from pylitmus.utils.exceptions import LibraryException


# Package env var prefix.
_PREFIX = 'LITMUS_'


class InvalidEnvironmentVariable(LibraryException):
    """Raised when a library environment variable has been misconfigured.
    
    """
    def __init__(self, name, val, expected=None):
        """Constructor.

        :param name: Environment variable name.
        :param val: Environment variable val.
        :param expected: Expected value.

        """ 
        err = f"Invalid env-var: {get_evar_name(name)} :: f{val}"
        if expected:
            if isinstance(expected, dict):
                expected = " | ".join(list(expected.keys()))
            err = f"{err}.  Expected {expected}"
        super(InvalidEnvironmentVariable, self).__init__(err)


def get_evar(
    name: str,
    default=None,
    convertor: typing.Callable=None
    ) -> str:
    """Returns an environment variable's current value.

    :param name: Environment variable name.
    :param default: Environment variable default value.
    :param convertor: Value conversion function to apply.
    :returns: An environment variable's current value.

    """
    value = os.getenv(get_evar_name(name)) or default

    return value if convertor is None or value is None else convertor(value)


def get_evar_name(name: str) -> str:
    """Returns an environment variable's name.

    :param name: Environment variable name.
    :returns: An environment variable's full name.

    """
    return f"{_PREFIX}{name.upper()}"
