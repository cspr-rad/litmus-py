import json

from pylitmus.cache.keys import era_info as ckey
from pylitmus.cache.model import Key
from pylitmus.cache.model import Partition
from pylitmus.cache.stores import get_store
from pylitmus.types import EraInfo


def get(era_id: int) -> bytes:
    """Decaches verified era information.

    :param block_id: Block identifier.
    :returns: Verified block information.

    """
    key: Key = ckey.from_id(era_id)
    with get_store(Partition.BLOCKS) as store:
        return store.get_one_from_many(key)


def set(entity: EraInfo) -> str:
    """Encaches a verified era.

    :param entity: Era information to be cached.
    :returns: Cache key.

    """
    with get_store(Partition.ERAS) as store:
        return store.set_one_singleton(
            ckey.from_self(entity),
            json.dumps(entity.to_dict()),
        )
