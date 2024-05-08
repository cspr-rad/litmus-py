import enum

from pylitmus.cache import store_redis
from pylitmus.cache import store_redis_fake
from pylitmus.cache.model import StorePartition
from pylitmus.utils import env


class StoreType(enum.Enum):
    """Enumeration over set of cache operations.
    
    """
    REDIS = "REDIS"
    STUB = "STUB"


# Environment variables required by this module.
class EnvVars:
    STORE_TYPE: StoreType = \
        StoreType[env.get_evar("CACHE_STORE_TYPE", default=StoreType.REDIS.value)]


# Map: Cache store type -> factory.
FACTORIES = {
    StoreType.REDIS: store_redis,
    StoreType.STUB: store_redis_fake
}


def get_store(partition_type: StorePartition):
    """Returns a cache store ready to be used as a state persistence & flow control mechanism.

    :param partition_type: Type of partition to be instantiated.
    :returns: A cache store.

    """ 
    try:
        factory = FACTORIES[EnvVars.STORE_TYPE]
    except KeyError:
        raise InvalidEnvironmentVariable("CACHE_STORE_TYPE", EnvVars.STORE_TYPE, FACTORIES)

    return factory.get_store(partition_type)
