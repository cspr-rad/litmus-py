import enum

from pylitmus.cache.model import Backend
from pylitmus.cache.model import Partition
from pylitmus.cache.evars import BACKEND
from pylitmus.cache.stores.redis.proxy import Proxy as RedisProxy


def get_store(partition: Partition):
    """Returns a backend proxy ready to be used as a state persistence & flow control mechanism.

    :param partition: Type of store partition.
    :returns: A backend proxy.

    """ 
    if BACKEND in {Backend.REDIS, Backend.REDIS_FAKE}:
        return RedisProxy(BACKEND, partition)
    else:
        raise ValueError("Invalid cache store type.")
