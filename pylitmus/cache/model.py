import dataclasses
import enum
import json
import typing


# Cache key separators.
_SEPERATOR_NAME: str = " || "
_SEPERATOR_PATH: str = " :: "
_SEPERATOR_KEY: str = ":"


@dataclasses.dataclass
class Entity():
    """An item to be encached alongside it's key.
    
    """
    key: str
    data: typing.Any
    expiration: int = None


@dataclasses.dataclass
class EntityKey():
    """A key of an encached item.
    
    """
    key: str

    @staticmethod
    def create(paths: typing.List[str], names: typing.List[str]) -> "EntityKey":
        path = _SEPERATOR_PATH.join([str(i) for i in paths])
        name = _SEPERATOR_NAME.join([str(i) for i in names])

        return EntityKey(f"{path}{_SEPERATOR_KEY}{name}")


@dataclasses.dataclass
class CountDecrementKey(EntityKey):
    """A key used to decrement a counter.
    
    """
    amount: int

    @staticmethod
    def create(paths: typing.List[str], names: typing.List[str], amount: int) -> EntityKey:
        path = _SEPERATOR_PATH.join([str(i) for i in paths])
        name = _SEPERATOR_NAME.join([str(i) for i in names])

        return CountDecrementKey(f"{path}{_SEPERATOR_KEY}{name}", amount)


@dataclasses.dataclass
class CountIncrementKey(EntityKey):
    """A key used to increment a counter.
    
    """
    amount: int

    @staticmethod
    def create(paths: typing.List[str], names: typing.List[str], amount: int) -> EntityKey:
        path = _SEPERATOR_PATH.join([str(i) for i in paths])
        name = _SEPERATOR_NAME.join([str(i) for i in names])

        return CountIncrementKey(f"{path}{_SEPERATOR_KEY}{name}", amount)


@dataclasses.dataclass
class SearchKey():
    """A key used to increment a counter.
    
    """
    key: str

    @staticmethod
    def create(paths: typing.List[str], wildcard="*") -> "SearchKey":
        path = _SEPERATOR_PATH.join([str(i) for i in paths])

        return SearchKey(f"{path}{wildcard}")


class StoreOperation(enum.Enum):
    """Enumeration over set of cache operations.
    
    """
    # Atomically increment a counter.
    COUNTER_INCR = enum.auto()

    # Atomically decrement a counter.
    COUNTER_DECR = enum.auto()

    # Delete a key.
    DELETE_ONE = enum.auto()

    # Flush a key set.
    DELETE_MANY = enum.auto()
    
    # Get count of matched cache item.
    GET_COUNT = enum.auto()

    # Get value of a cached counter.
    GET_COUNTER_ONE = enum.auto()

    # Get value of many cached counters.
    GET_COUNTER_MANY = enum.auto()

    # Get a single cached item.
    GET_ONE = enum.auto()

    # Get a single cached item from a collection.
    GET_ONE_FROM_MANY = enum.auto()

    # Get a collection of cached items.
    GET_MANY = enum.auto()

    # Set an item.
    SET_ONE = enum.auto()

    # Set cached item plus flag indicating whether it already was cached.
    SET_ONE_SINGLETON = enum.auto()


class StorePartition(enum.Enum):
    """Enumeration over set of store partitions.
    
    """
    # Block data.
    BLOCKS = enum.auto()

    # Merkle proof data.
    MERKLE_PROOFS = enum.auto()
