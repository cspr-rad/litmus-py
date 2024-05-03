import enum
import json
import typing


class CacheItem():
    """An item to be encached alongside it's key.
    
    """
    def __init__(self, item_key: CacheItemKey, data: typing.Any, expiration: int = None):
        self.key = item_key.key
        self.data = data
        self.expiration = expiration

    @property
    def data_as_json(self):
        return json.dumps(encoder.encode(self.data), indent=4)


class CacheItemKey():
    """A key of an encached item.
    
    """
    def __init__(self, paths: typing.List[str], names: typing.List[str]):
        path = ":".join([str(i) for i in paths])
        name = ".".join([str(i) for i in names])
        self.key = f"{path}:{name}"


class CountDecrementKey(CacheItemKey):
    """A key used to decrement a counter.
    
    """
    def __init__(self, paths: typing.List[str], names: typing.List[str], amount: int):
        super().__init__(paths, names)
        self.amount = amount


class CountIncrementKey(CacheItemKey):
    """A key used to increment a counter.
    
    """
    def __init__(self, paths: typing.List[str], names: typing.List[str], amount: int):
        super().__init__(paths, names)
        self.amount = amount
        

class CacheSearchKey():
    """A key used to perform a cache search.
    
    """
    def __init__(self, paths: typing.List[str], wildcard="*"):
        path = ':'.join([str(i) for i in paths])
        self.key = f"{path}{wildcard}"


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
    BLOCK = enum.auto()

    # Merkle proof data.
    MERKLE_PROOFS = enum.auto()
