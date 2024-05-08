import enum

from pylitmus.cache.model import Entity
from pylitmus.cache.model import EntityKey
from pylitmus.cache.model import StoreOperation
from pylitmus.cache.model import StorePartition
from pylitmus.cache.utils import cache_op
from pylitmus.chain import Block


# Cache partition.
_PARTITION = StorePartition.BLOCKS


class _COLLECTIONS(enum.Enum):
    """Enumeration over set of partition collection.
    
    """
    BLOCKS = "block"


@cache_op(_PARTITION, StoreOperation.SET_ONE)
def set_verified_block(data: Block) -> Entity:
    """Encaches domain entity instance: Block.

    :param data: Data to be cached.

    :returns: Cache entity.

    """
    return Entity(
        key=EntityKey.create(
            paths=[
                _COLLECTIONS.BLOCKS.value,
            ],
            names=[
                str(data.header.height).zfill(12),
                data.hash.hex(),
                data.header.parent_hash.hex(),
            ]
        ).key,
        data=data.hash.hex()
        )
