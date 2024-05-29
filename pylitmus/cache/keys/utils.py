import typing

from pylitmus.cache.model import Key


# Key separators.
_SEPERATOR_NAME: str = " || "
_SEPERATOR_PATH: str = "."
_SEPERATOR_KEY: str = ":"


def get_key(paths: typing.List[str], names: typing.List[str]) -> Key:
    """Returns a formatted cache key.
    
    :params paths: Set of cache entity paths.
    :params names: Set of cache entity names.
    :returns: A formatted cache key.

    """
    path: str = _SEPERATOR_PATH.join([str(i) for i in paths])
    name: str = _SEPERATOR_NAME.join([str(i) for i in names])

    return f"{path}{_SEPERATOR_KEY}{name}"
