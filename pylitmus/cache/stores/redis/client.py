import fakeredis
import redis

from pylitmus.cache import evars
from pylitmus.cache.model import Backend
from pylitmus.cache.model import StorePartition


# Map: store partition <-> db offset.
PARTITION_OFFSET = {
    StorePartition.BLOCKS: 1,
    StorePartition.MERKLE_PROOFS: 2,
}


def get_client(backend: Backend, partition: StorePartition):
    """Returns a cache client ready to be used as a state persistence & flow control mechanism.

    :params store_type: Type ofache store to be utilised.
    :param partition: Type of partition to be instantiated.
    :returns: A cache store.

    """ 
    if backend == Backend.REDIS:
        return redis.Redis(
            db=evars.REDIS_DB + PARTITION_OFFSET[partition],
            host=evars.REDIS_HOST,
            port=evars.REDIS_PORT,
        )

    elif backend == Backend.REDIS_FAKE:
        return fakeredis.FakeStrictRedis()

    else:
        raise ValueError("Invalid cache store type.")
