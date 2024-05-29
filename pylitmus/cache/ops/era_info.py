import json

from pylitmus.cache.keys import era_info as ckey
from pylitmus.cache.model import Partition
from pylitmus.cache.stores import get_store
from pylitmus.types import EraConsensusWeights


def set(entity: EraConsensusWeights) -> str:
    """Encaches a verified era.

    :param entity: Era information to be cached.
    :returns: Cache key.

    """
    with get_store(Partition.ERAS) as store:
        return store.set_one_singleton(
            ckey.from_self(entity),
            json.dumps(entity.to_dict()),
        )
