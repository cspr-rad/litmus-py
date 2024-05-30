import json

from pylitmus.cache.keys import block_info as ckey
from pylitmus.cache.model import Partition
from pylitmus.cache.stores import get_store
from pylitmus.types import BlockInfo


def set(entity: BlockInfo) -> str:
    """Encaches verified block information.

    :param entity: Block information to be cached.
    :returns: Cache key.

    """
    with get_store(Partition.BLOCKS) as store:
        return store.set_one_singleton(
            ckey.from_self(entity),
            json.dumps(entity.to_dict()),
        )
