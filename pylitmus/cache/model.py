import dataclasses
import enum
import json
import typing


# Cache key separators.
_SEPERATOR_NAME: str = " || "
_SEPERATOR_PATH: str = "."
_SEPERATOR_KEY: str = ":"


@dataclasses.dataclass
class Entity():
    """An item to be encached alongside it's key.
    
    """
    # Cache key.
    key: str

    # Data to be encached.
    data: typing.Any

    # Expiration in milliseconds.
    expiration: int = None


class EntityKey():
    """A key of an encached item.
    
    """
    @staticmethod
    def create(paths: typing.List[str], names: typing.List[str]) -> str:
        path = _SEPERATOR_PATH.join([str(i) for i in paths])
        name = _SEPERATOR_NAME.join([str(i) for i in names])

        return f"{path}{_SEPERATOR_KEY}{name}"


@dataclasses.dataclass
class CounterKey():
    """A key used to manage a counter.
    
    """
    # Cache key.
    key: str

    # Increment ordinal.
    amount: int


@dataclasses.dataclass
class CountDecrementKey(CounterKey):
    """A key used to decrement a counter.
    
    """
    @staticmethod
    def create(paths: typing.List[str], names: typing.List[str], amount: int) -> "CountDecrementKey":
        path = _SEPERATOR_PATH.join([str(i) for i in paths])
        name = _SEPERATOR_NAME.join([str(i) for i in names])

        return CountDecrementKey(f"{path}{_SEPERATOR_KEY}{name}", amount)


@dataclasses.dataclass
class CountIncrementKey(CounterKey):
    """A key used to increment a counter.
    
    """
    @staticmethod
    def create(paths: typing.List[str], names: typing.List[str], amount: int) -> "CountIncrementKey":
        path = _SEPERATOR_PATH.join([str(i) for i in paths])
        name = _SEPERATOR_NAME.join([str(i) for i in names])

        return CountIncrementKey(f"{path}{_SEPERATOR_KEY}{name}", amount)


class StorePartition(enum.Enum):
    """Enumeration over set of store partitions.
    
    """
    # Block data.
    BLOCKS = enum.auto()

    # Merkle proof data.
    MERKLE_PROOFS = enum.auto()
