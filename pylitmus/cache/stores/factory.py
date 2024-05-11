import enum

from pylitmus.cache.model import StorePartition
from pylitmus.utils import env
from pylitmus.cache.stores.redis.proxy import Proxy as RedisProxy
from pylitmus.cache.stores.types import BACKEND
from pylitmus.cache.stores.types import Backend


def get_proxy(partition: StorePartition):
    """Returns a backend proxy ready to be used as a state persistence & flow control mechanism.

    :param partition: Type of store partition.
    :returns: A backend proxy.

    """ 
    if BACKEND in {Backend.REDIS, Backend.REDIS_FAKE}:
        return RedisProxy(BACKEND, partition)
    else:
        raise ValueError("Invalid cache store type.")
