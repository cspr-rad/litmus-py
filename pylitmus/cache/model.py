import dataclasses
import enum
import json
import typing


# Cache key separators.
_SEPERATOR_NAME: str = " || "
_SEPERATOR_PATH: str = "."
_SEPERATOR_KEY: str = ":"


class CacheKey():
    """A key of an encached item.
    
    """
    @staticmethod
    def create(paths: typing.List[str], names: typing.List[str]) -> str:
        path = _SEPERATOR_PATH.join([str(i) for i in paths])
        name = _SEPERATOR_NAME.join([str(i) for i in names])

        return f"{path}{_SEPERATOR_KEY}{name}"


class Backend(enum.Enum):
    """Enumeration over set of supported backends.
    
    """
    REDIS = "REDIS"
    REDIS_FAKE = "REDIS_FAKE"


class StorePartition(enum.Enum):
    """Enumeration over set of store partitions.
    
    """
    # Block data.
    BLOCKS = enum.auto()

    # Merkle proof data.
    MERKLE_PROOFS = enum.auto()
