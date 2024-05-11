import enum


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
