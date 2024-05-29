import enum
import typing


Key = typing.NewType(
    "Entity cache key.", str
    )


class Backend(enum.Enum):
    """Enumeration over set of supported backends.
    
    """
    REDIS = "REDIS"
    REDIS_FAKE = "REDIS_FAKE"


class Partition(enum.Enum):
    """Enumeration over set of store partitions.
    
    """
    # Verified block data.
    BLOCKS = enum.auto()

    # Verified deploy data.
    DEPLOYS = enum.auto()

    # Verified era data.
    ERAS = enum.auto()

    # Verified state proofs.
    MERKLE_PROOFS = enum.auto()
