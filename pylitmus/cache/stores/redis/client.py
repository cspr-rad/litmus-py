import fakeredis
import redis

from pylitmus.cache import evars
from pylitmus.cache.model import Backend
from pylitmus.cache.model import Partition


# Map: store partition <-> db offset.
PARTITION_OFFSET = {
    Partition.BLOCKS: 1,
    Partition.DEPLOYS: 1,
    Partition.ERAS: 1,
    Partition.MERKLE_PROOFS: 1,
}


def get_client(backend: Backend, partition: Partition) -> object:
    """Returns a cache client ready to be used as a state persistence & flow control mechanism.

    :params backend: Type of cache backend being utilised.
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
